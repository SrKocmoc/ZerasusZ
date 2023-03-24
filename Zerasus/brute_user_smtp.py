import socket,sys
from time import sleep
from colores import color, select_option, select_proxymain
from Zerasus import menu

try:
    select_option()
    select_proxymain()
    option = int(input('-> '))

    print(f"{color.CYAN_BG}[ X ] Informe a Lista de Nomes [ X ]\n")
    nomes = open(input(f"-> {color.END}"), 'rt', encoding='latin')


    def smtp_proxyno():

        for nome in nomes.readlines():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((sys.argv[1], 25))
            data = s.recv(1024)
            print(data)

            s.send(bytes(f'VRFY {nome}\r\n'.encode('utft-8')))
            print(s.recv(1024))


    def smtp_proxyes():
        for nome in nomes.readlines():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((sys.argv[1], 25))
            data = s.recv(1024)
            print(data)

            s.send(bytes(f'VRFY {nome}\r\n'.encode('utft-8')))
            print(s.recv(1024))

    if option == 1:
        smtp_proxyno()
    elif option == 2:
        smtp_proxyes()
    else:
        print(f"{color.RED}Na proxima informe uma opcao!")
        sleep(3)
        print(f"De volta para o menu!{color.END}")
        sleep(2)
        menu()

except Exception:
    print(f"{color.RED}Ocorreu um Erro: {Exception}")
    sleep(3)
    print(f'De volta para o Menu!{color.END}')
    sleep(2)
    menu()
