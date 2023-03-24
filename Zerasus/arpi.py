import socket
import scapy.all as scapy
from time import sleep
from Zerasus import menu
from colores import color

try:
    def Arp(ip):
        ip = ip
        print(ip)
        arp_r = scapy.ARP(pdst=ip)
        br = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        request = br / arp_r
        answered, unanswered = scapy.srp(request, timeout=1)
        print(f'{color.CYAN}\tIP\t\tMAC{color.END}')
        print(f'{color.GREEN}_{color.END}' * 37)
        for i in answered:
            sleep(0.25)
            ip, mac = i[1].psrc, i[1].hwsrc
            print(f"{color.GREEN}{ip}\t{mac}{color.END}")
            print(f'{color.GREEN}_{color.END}' * 37)


    Arp(input(f"{color.GREEN}exp: 192.168.1.0/24\nInforme a rede:{color.END}"))
except socket.gaierror as err:
    print(f"{color.RED}Ocorreu um erro: {err}")
    sleep(3)
    print(f'De volta para o Menu!{color.END}')
    sleep(2)
    menu()
