import dns.zone
import dns.resolver
from time import sleep
from colores import color,clear, select_url, select_option, select_proxymain
from Zerasus import menu
from proxyis import proxis

try:
    select_option()
    select_proxymain()
    option = int(input('-> '))

    my_resolver = dns.resolver.Resolver()
    ns_servers = []
    select_url()
    business_name = input(f"-> ")
    clear()

    def dns_zone1(address):
        global ip, server, ip_answer
        ns_answer = my_resolver.resolve(address, 'NS')
        for server in ns_answer:
            print(f"{color.BLUE}[ - ]{color.END} NS Encontrado: {server} {color.BLUE}[ - ]{color.END}")
            ip_answer = my_resolver.resolve(server.target, 'A')
        for ip in ip_answer:
            print(f"{color.BLUE}[ ._. ]{color.END} IP {server} is {ip} {color.BLUE}[ ._. ]{color.END}")
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(str(ip), address))
                for host in zone:
                    print(f"{color.GREEN}[ :3 ]{color.END} Host Encontrado: {host}")
                sleep(5)
                menu()

            except Exception:
                print(f"[ :( ] NS {server} Transferencia de Zona recusada! [ :( ]")
                sleep(3)
                echo = input("Dica: As vezes eh bom tentar mais de 3x...\r\nQuer tentar novamente [S or N]?")
                if echo == "S":
                    dns_zone1(business_name)
                else:
                    pass

    if option == 1:
        dns_zone1(business_name)
    elif option == 2:
        proxis()
        dns_zone1(business_name)
    else:
        print(f"{color.RED}Na proxima informe uma opcao!")
        sleep(3)
        print(f"De volta para o menu!{color.END}")
        sleep(2)
        menu()
except Exception:
    print(f"{color.RED}[ ! ] Ocorreu um Erro: {Exception}")
    sleep(2)
    print(f'De volta para o Menu!{color.END}')
    sleep(3)
    menu()
