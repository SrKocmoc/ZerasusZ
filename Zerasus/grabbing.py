import requests
import re
from colores import *
from Zerasus import menu
from proxyis import proxis

try:
    clear()
    select_option()
    select_proxymain()
    option = int(input('-> '))

    def grabing_no_proxy():
        host = requests.get(input(f"{color.RED}Exp: https://site.com.br{color.END}\r\n{color.GREEN}Informe a url > {color.END}"))
        print()
        # E-mails
        eco = re.findall(r'[\w\.-]+@[\w\.-]+', host.text)

        arquivo = open(f"{host.url.replace('/', '')}.txt", 'a')
        arquivo.writelines(f'\nEmails: {eco}')
        arquivo.close()

        # Https
        doc = re.findall("https://.*/.*/", str(host.text))
        for dc in doc:
            htps = re.findall('https://.*/.*/', dc)
            arquivo = open(f"{host.url.replace('/', '')}.txt", 'a')
            arquivo.writelines(f'\nHttps: {htps}')
            arquivo.close()

        # HTTP
        xoc = re.findall("http://.*/.*/", str(doc))
        for i in xoc:
            d = re.findall('://.*', i)
            for c in str(d).replace(',', '\r\n').splitlines():
                htt = re.findall(":.*http://*.*.*", c)
                if not htt:
                    pass
                else:
                    arquivo = open(f"{host.url.replace('/', '')}.txt", 'a')
                    arquivo.writelines(f'\nHttp: {htt}')
                    arquivo.close()

        # Scripts
        scr = re.findall("<script*..*>.*</script>", str(host.text))
        for script in scr:
            arquivo = open(f"{host.url.replace('/', '')}.txt", 'a')
            arquivo.writelines(f'\nScripts: {script}')
            arquivo.close()

        # Telefone
        fon = re.findall('phone.*.*', str(host.text))
        fon2 = re.findall('fone.*.*', str(host.text))
        for fone in fon2 and fon:
            arquivo = open(f"{host.url.replace('/', '')}.txt", 'a')
            arquivo.writelines(f"\nTelefone: {fone[0:28].replace('</span>', '')}")
            arquivo.close()
        print(f"Salvo como: {host.url.replace('/', '')}.txt")
        sleep(5)
        menu()


    if option == 1:
        clear()
        grabing_no_proxy()
    elif option == 2:
        clear()
        proxis()
        grabing_no_proxy()
    else:
        print(f"{color.RED}Na proxima informe uma opcao!", sleep(3))
        clear()
        print(f"De volta para o menu!{color.END}", (2))
        menu()
except ValueError:
    print(f"{color.RED}Resposta errada! Eu esperava numero nao string...")
    sleep(2)
    print(f"De volta para o Menu!{color.END}")
    sleep(3)
    menu()
