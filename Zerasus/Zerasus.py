from colores import *


def menu():
    intro()
    clear()
    select_option()
    print(f"[{color.GREEN}1{color.END}]{color.RED}  GitCl0ne - @Abdularah33m     {color.END}\n"
          f"[{color.GREEN}2{color.END}]{color.RED}  Black Bird - P1ngul1n0       {color.END}\n"
          f"[{color.GREEN}3{color.END}]{color.RED}  BoF  (Buffer overflow)       {color.END}\n"
          f"[{color.GREEN}4{color.END}]{color.RED}  DoS  (Denial of Service)     {color.END}\n"
          f"[{color.GREEN}5{color.END}]{color.RED}  Port Scanning                {color.END}\n"
          f"[{color.GREEN}6{color.END}]{color.RED}  Zone Transfer                {color.END}\n"
          f"[{color.GREEN}7{color.END}]{color.RED}  DnS Resolver                 {color.END}\n"
          f"[{color.GREEN}8{color.END}]{color.RED}  Brute Hashes                 {color.END}\n"
          f"[{color.GREEN}9{color.END}]{color.RED} Facebook Hacking              {color.END}\n"
          f"[{color.GREEN}10{color.END}]{color.RED} Instagram Hacking            {color.END}\n"
          f"[{color.GREEN}11{color.END}]{color.RED} Brute SSH                    {color.END}\n"
          f"[{color.GREEN}12{color.END}]{color.RED} Brute SMTP                   {color.END}\n"
          f"[{color.GREEN}13{color.END}]{color.RED} Brute FTP                    {color.END}\n"
          f"[{color.GREEN}14{color.END}]{color.RED} Arp Recon                    {color.END}\n"
          f"[{color.GREEN}15{color.END}]{color.RED} Web Grabbing                 {color.END}\n"
          )

    option = input(f"{color.GREEN}\n-> {color.END}")

    if option == "1":
        import Cl0neMast3r
    elif option == "2":
        import blackbird
    elif option == "3":
        import BoF
    elif option == "4":
        import dos
    elif option == "5":
        import port_scanning
    elif option == "6":
        import zone_transfer
    elif option == "7":
        import resolver
    elif option == "8":
        import brute_force_hash
    elif option == "9":
        import facebook
    elif option == "10":
        import instagram
    elif option == "11":
        import brute_ssh
    elif option == "12":
        import brute_user_smtp
    elif option == "13":
        import brute_ftp
    elif option == "14":
        import arpi
    elif option == "15":
        import grabbing


if __name__ == "__main__":
    menu()
