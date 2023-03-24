import asyncio
import json
import os
import random
import sys
import time
from colores import color
import warnings
from datetime import datetime
from colores import select_option, select_username, select_proxymain, sleep, clear
from proxyis import proxis
import aiohttp
from Zerasus import menu
from bs4 import BeautifulSoup
from colorama import Fore, init

file = open('data.json')
searchData = json.load(file)
currentOs = sys.platform
path = os.path.dirname(__file__)
warnings.filterwarnings('ignore')

useragents = open('useragents.txt').read().splitlines()


async def findUsername(username, interfaceType):
    start_time = time.time()
    timeout = aiohttp.ClientTimeout(total=20)

    print(f"{Fore.LIGHTYELLOW_EX}[!] Searching '{username}' across {len(searchData['sites'])} social networks\033[0m")

    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = []
        for u in searchData["sites"]:
            task = asyncio.ensure_future(makeRequest(session, u, username, interfaceType))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        executionTime = round(time.time() - start_time, 1)
        userJson = {"search-params": {"username": username, "sites-number": len(searchData['sites']), "date": now,
                                      "execution-time": executionTime}, "sites": []}
        for x in results:
            userJson["sites"].append(x)
        pathSave = os.path.join(path, 'results', username + '.json')
        userFile = open(pathSave, 'w')
        json.dump(userJson, userFile, indent=4, sort_keys=True)

        print(f"{Fore.LIGHTYELLOW_EX}[!] Search complete in {executionTime} seconds\033[0m")
        print(f"{Fore.LIGHTYELLOW_EX}[!] Results saved to {username}.json\033[0m")
        return userJson


async def makeRequest(session, u, username, interfaceType):
    url = u["url"].format(username=username)
    jsonBody = None
    useragent = random.choice(useragents)
    headers = {
        "User-Agent": useragent
    }
    metadata = []
    if 'headers' in u:
        headers.update(eval(u['headers']))
    if 'json' in u:
        jsonBody = u['json'].format(username=username)
        jsonBody = json.loads(jsonBody)
    try:
        async with session.request(u["method"], url, json=jsonBody, headers=headers,
                                   ssl=False) as response:
            responseContent = await response.text()
            if 'content-type' in response.headers and "application/json" in response.headers["Content-Type"]:
                await response.json()
            else:
                soup = BeautifulSoup(responseContent, 'html.parser')

            if eval(u["valid"]):
                print(
                    f'{Fore.LIGHTGREEN_EX}[+]\033[0m - #{u["id"]} {Fore.BLUE}{u["app"]}\033[0m {Fore.LIGHTGREEN_EX}account found\033[0m - {Fore.YELLOW}{url}\033[0m [{response.status} {response.reason}]\033[0m')
                if 'metadata' in u:
                    metadata = []
                    for d in u["metadata"]:
                        try:
                            value = eval(d['value']).strip('\t\r\n')
                            print(f"   |--{d['key']}: {value}")
                            metadata.append({"type": d["type"], "key": d['key'], "value": value})
                        except Exception as e:
                            pass
                return (
                {"id": u["id"], "app": u['app'], "url": url, "response-status": f"{response.status} {response.reason}",
                 "status": "FOUND", "error-message": None, "metadata": metadata})
            else:
                if interfaceType == 'CLI':
                    if showAll:
                        print(
                            f'[-]\033[0m - #{u["id"]} {Fore.BLUE}{u["app"]}\033[0m account not found - {Fore.YELLOW}{url}\033[0m [{response.status} {response.reason}]\033[0m')
                return (
                {"id": u["id"], "app": u['app'], "url": url, "response-status": f"{response.status} {response.reason}",
                 "status": "NOT FOUND", "error-message": None, "metadata": metadata})
    except Exception as e:
        if interfaceType == 'CLI':
            if showAll:
                print(
                    f'{Fore.RED}[X]\033[0m - #{u["id"]} {Fore.BLUE}{u["app"]}\033[0m error on request ({repr(e)})- {Fore.YELLOW}{url}\033[0m')
        return ({"id": u["id"], "app": u['app'], "url": url, "response-status": None, "status": "ERROR",
                 "error-message": repr(e), "metadata": metadata})


def list_sites():
    for i, u in enumerate(searchData["sites"], 1):
        print(f'{i}. {u["app"]}')


def read_results(file):
    try:
        pathRead = os.path.join(path, 'results', file)
        f = open(pathRead, 'r')
        jsonD = json.load(f)
        print(f'Loaded results file: {file}')
        print(f"Username: {jsonD['search-params']['username']}")
        print(f"Number of sites: {jsonD['search-params']['sites-number']}")
        print(f"Date: {jsonD['search-params']['date']}")
        print('-------------------------------------------------')
        for u in jsonD['sites']:
            if u['status'] == "FOUND":
                print(
                    f'{Fore.LIGHTGREEN_EX}[+]\033[0m - {Fore.BLUE}{u["app"]}\033[0m {Fore.LIGHTGREEN_EX}account found\033[0m - {Fore.YELLOW}{u["url"]}\033[0m [{u["response-status"]}]\033[0m')
                if u["metadata"]:
                    for d in u["metadata"]:
                        print(f"   |--{d['key']}: {d['value']}")
            elif u['status'] == "ERROR":
                print(
                    f'{Fore.RED}[X]\033[0m - {Fore.BLUE}{u["app"]}\033[0m error on request ({u["error-message"]}) - {Fore.YELLOW}{u["url"]}\033[0m')
            elif u['status'] == "NOT FOUND":
                print(
                    f'{Fore.WHITE}[-]\033[0m - {Fore.BLUE}{u["app"]}\033[0m account not found - {Fore.YELLOW}{u["url"]}\033[0m [{u["response-status"]}]\033[0m')

    except Exception as e:
        print(f'{Fore.RED}[X] Error reading file [{repr(e)}]')


init()
clear()
print(Fore.RED + f"""
▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀ ▄▄▄▄    ██▓ ██▀███  ▓█████▄ 
▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█████▄ ▓██▒▓██ ▒ ██▒▒██▀ ██▌
▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▒ ▄██▒██▒▓██ ░▄█ ▒░██   █▌
▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒██░█▀  ░██░▒██▀▀█▄  ░▓█▄   ▌
░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▓█  ▀█▓░██░░██▓ ▒██▒░▒████▓ 
░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▒▓███▀▒░▓  ░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░▒░▒   ░  ▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ 
░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░  ░    ░  ▒ ░  ░░   ░  ░ ░  ░ 
░          ░  ░     ░  ░░ ░      ░  ░    ░       ░     ░        ░    
    ░                  ░                     ░               ░      

                                    Made with ❤️️ ------------ by {Fore.BLUE}p1ngul1n0  Github: https://github.com/p1ngul1n0/blackbird\n""")

print('An OSINT tool to search for accounts by username in social networks.')

select_option()
select_proxymain()
option = int(input('-> '))
clear()

select_username()
user = input(f'-> ')
clear()

print(f"{color.CYAN_BG}[ X ] Mostrar Requests  S ou N [ X ]\n{color.END}{color.END}")
view = input("-> ")
clear()

if option == 1:
    pass
elif option == 2:
    proxis()
    sleep(2)
    clear()
    pass
else:
    print(f"{color.RED}Na proxima informe uma opcao!")
    sleep(3)
    print(f"De volta para o menu!{color.END}")
    sleep(2)
    menu()

if view.lower() == 's':
    clear()
    showAll = True
elif view.lower() == 'n':
    clear()
    showAll = False

try:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
except:
    pass
interfaceType = 'CLI'
asyncio.run(findUsername(user, interfaceType))
