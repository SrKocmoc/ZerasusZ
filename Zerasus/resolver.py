import dns.resolver
import re
from Zerasus import menu
from colores import color, select_url, select_option, select_proxymain
from time import sleep
from proxyis import proxis
import requests,json

try:
    select_option()
    select_proxymain()
    option = int(input('-> '))

    select_url()
    domain = input(f"{color.CYAN_BG}-> {color.END}")

    def resolver():

        flag = ['NS', 'MX', 'TXT', 'PTR', 'SOA', 'CNAME', 'A', 'AAAA', 'AXFR', 'DNSKEY', 'IXFR', 'HINFO']
        for i in flag:
            try:
                dx = dns.resolver.resolve(domain, i)
                for c in dx:
                    if i == "NS":
                        print(f"{color.BOLD}Name Server: {color.END}{color.UNDERLINE}{c}{color.END}")
                    elif i == 'MX':
                        print(f"{color.BOLD}Mail Server: {color.END}{color.UNDERLINE}{c}{color.END}")
                    elif i == 'TXT':
                        if re.findall('[\w\.?]all', str(c)):
                            print(f"{color.BOLD}Registro TXT: {color.END}{color.UNDERLINE}{c} - Suscetivel a SPF{color.END}")
                        elif re.findall('~all', str(c)):
                            print(f"{color.BOLD}Registro TXT: {color.END}{color.UNDERLINE}{c} - Suscetivel a SPF{color.END}")
                        elif re.findall('.-all', str(c)):
                            print(f"{color.BOLD}Registro TXT: {color.END}{color.UNDERLINE}{c} - Nao vulneravel a SPF{color.END}")
                        elif not re.findall('all', str(c)):
                            print(f"{color.BOLD}Registro TXT: {color.END}{color.UNDERLINE}{c} - Vulneravel a SPF{color.END}")
                    elif i == 'PTR':
                        print(f"{color.BOLD}PTR: {color.END}{color.UNDERLINE}{c}{color.END}")
                    elif i == 'SOA':
                        print(f"{color.BOLD}SOA: {color.END}{color.UNDERLINE}{c}{color.END}")
                    elif i == 'CNAME':
                        print(f"{color.BOLD}CNAME: {color.END}{color.UNDERLINE}{c}{color.END}")
                    elif i == 'A':
                        print(f"{color.BOLD}IPV4 Address: {color.END}{color.UNDERLINE}{c}{color.END}")
                    elif i == 'AAAA':
                        print(f"{color.BOLD}IPV6 Address: {color.END}{color.UNDERLINE}{c}{color.END}")
                    elif i == 'AXFR':
                        print(f"{color.BOLD}AXFR: {color.END}{color.UNDERLINE}{c}{color.END}")
                    elif i == 'DNSKEY':
                        print(f"{color.BOLD}DNSKEY: {color.END}{color.UNDERLINE}{c}{color.END}")
                    elif i == 'IXFR':
                        print(f"{color.BOLD}IXFR: {color.END}{color.UNDERLINE}{c}{color.END}")
                    elif i == 'HINFO':
                        print(f"{color.BOLD}HINFO: {color.END}{color.UNDERLINE}{c}{color.END}")
            except:
                pass

    if option == 1:
        resolver()
    elif option == 2:
        proxis()
        resolver()
    else:
        print(f"{color.RED}Na proxima informe uma opcao!")
        sleep(3)
        print(f"De volta para o menu!{color.END}")
        sleep(2)
        menu()
except Exception as err:
    print(f"{color.RED}Ocorreu um erro: {err}")
    sleep(2)
    print(f'De volta para o Menu!{color.END}')
    sleep(3)
    menu()
