import json
import socket
import pyChainedProxy as socks
import requests
from time import sleep


# Caso tenha erro com proxy descomente:
# def DEBUG(msg):
#     print(msg)
# socks.DEBUG = DEBUG

def proxis():
    ca = requests.get('http://ip-api.com/json').content
    dx = json.loads(ca)
    print(f"Seu antigo local: {dx['countryCode']}")

    chain = [
        'socks://localhost:9050/'# First hop is Tor,
    ]

    socks.setdefaultproxy()  # Clear the default chain

    for hop in chain:
        socks.adddefaultproxy(*socks.parseproxy(hop))

    socks.setproxy('localhost', socks.PROXY_TYPE_TOR)
    socks.setproxy('127.0.0.1', socks.PROXY_TYPE_TOR)

    rawsocket = socket.socket
    socket.socket = socks.socksocket

    ca = requests.get('http://ip-api.com/json').content
    dx = json.loads(ca)
    print(f"Seu novo local: {dx['countryCode']}")


def proxy_fb():
    ca = requests.get('http://ip-api.com/json').content
    dx = json.loads(ca)
    print(f"Antigo local: {dx['countryCode']}")
    chain = [
        'socks://localhost:9050/'
    ]

    socks.setdefaultproxy()

    for hop in chain:
        socks.adddefaultproxy(*socks.parseproxy(hop))

    socks.setproxy('localhost', socks.PROXY_TYPE_TOR)
    socks.setproxy('127.0.0.1', socks.PROXY_TYPE_TOR)

    rawsocket = socket.socket
    socket.socket = socks.socksocket

    ca = requests.get('http://ip-api.com/json').content
    dx = json.loads(ca)
    print(f"Seu novo local: {dx['countryCode']}")

    while True:
        te = requests.get('http://ip-api.com/json').content
        a2 = json.loads(te)

        if a2['countryCode'] != "US":
            print('A aguardar..')
            print(a2["country"])
            sleep(200)

        else:
            break
    proxy_fb()
