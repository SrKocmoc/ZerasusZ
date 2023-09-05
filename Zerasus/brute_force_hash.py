import crypt
from Zerasus import menu
from colores import color
from time import sleep
try:

    word = input("Informe a wordlist: ")
    with open(word, "rt", encoding='latin') as file:

        a = input(f"{color.CYAN_BG}Informe o Salt: ")
        b = input(f"Infome a Hash completa: {color.END}")

        red = file.read().splitlines()
        for i in red:
            c = crypt.crypt(i, a)
            if b in c:
                print(f"{color.BLUE}Senha encontrada: {i}")
                man = input(f"Deseja ir de voltar para o mennu? [S or N] {color.END}")

                if man.islower() == "s":
                    menu()
                else:
                    print("Bye bye :)")
                    break
            else:
                print(f"{color.RED}Testando ----> {c} : {i}{color.END}")
except Exception:
    print(f"{color.RED}Ocorreu um Erro: {Exception}", sleep(3))
    print(f'De volta para o Menu!{color.END}', sleep(2))
    menu()
