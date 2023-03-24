import os
from time import sleep


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    CYAN_BG = '\33[1;37;40m'


def intro():
    os.system("clear")
    print(f"""{color.RED}
    _______________________________________\      |___________________________________
    |     ./\        /\.  KocmocHDA         \     |                                  |
    |    ./  \      /  \.                    \    |                                  |
    |   ./    \    /    \.                    \   |                                  |
    |  ./      \  /      \.  ZERASUS           \  |                                  |
    | ./    -   \/   0    \.  ---------------   \ |                                  |
    |./                    \.                    \|                                  |
    |--------------------------------------------------------------------------------|
    """)
    sleep(4)


def select_port():
    print(f"{color.CYAN_BG}[ X ] Input Port [ X ]{color.END}{color.END}")


def select_host():
    print(f"{color.CYAN_BG}[ X ] Input Host [ X ]\nEx: 127.0.0.1{color.END}{color.END}")


def select_url():
    print(f"{color.CYAN_BG}[ X ] Input url [ X ]\nEx: site.com{color.END}{color.END}")


def select_option():
    print(f"{color.CYAN_BG}[ X ] select an option [ X ]\n{color.END}{color.END}")


def select_wordlist():
    print(f"{color.CYAN_BG}[ X ] select wordlist [ X ]\n{color.END}{color.END}")


def select_username():
    print(f"{color.CYAN_BG}[ X ] enter username [ X ]\n{color.END}{color.END}")


def select_proxymain():
    print(f"[{color.GREEN}1{color.END}] Proxy[off]\r\n[{color.GREEN}2{color.END}] Proxy[on]")


def select_conections():
    print(f"{color.CYAN_BG}[ X ] Informe Quantas Conexoes [ X ]\n{color.END}{color.END}")


def select_threads():
    print(f"{color.CYAN_BG}[ X ] Informe Quantos Threads [ X ]\n{color.END}{color.END}")


def info_bytes():
    print(f"{color.CYAN_BG}[ X ] Informe Quantos Bytes [ X ]\n{color.END}{color.END}")


def info_EIP():
    print(f"{color.CYAN_BG}[ X ] Informe o EIP [ X ]\nEx: \XA0\X10\X12\X62 {color.END}{color.END}")


info_EIP()


def info_shellcode():
    print(f"{color.CYAN_BG}[ X ] Informe Quantos Threads [ X ]\n{color.END}{color.END}")


def info_msg():
    print(f"{color.CYAN_BG}[ X ] Informe o comando para o server [EXP: SEND, VRFY ] [ X ]\n{color.END}{color.END}")


def clear():
    os.system("clear")
