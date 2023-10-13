# coding: utf-8

import os
from Zerasus import menu
from re import search
from requests import get
from threading import Thread
from bs4 import BeautifulSoup
from datetime import datetime

# Adding some colors to the script
end = '\033[1;m'
red = '\033[1;31m'
white = '\033[1;37m'
green = '\033[1;32m'


class Tool:  # This class is responsible about Tools
    list = []
    toolNum = num = 1
    toolsFile = 'ToolsList.txt'
    htmlFile = 'ToolsList.html'
    access_token = '36464acb844fc53b9b8b2401da68844f6b05ebb0'  # GitHub API (You can use your access_token)

    def __init__(self, url, *add):  # Constructor
        url = self.getUrl(url)
        u = url[19:].split('/')
        self.author = u[0]
        self.name = u[1]
        self.url = url
        self.num = Tool.toolNum if add else Tool.num
        self.available = self.check(self.url)  # Check that the tool is available
        self.desc = self.getDescription() if self.available else None
        if add:  # If user wants to add the tool to the list
            if self.available:
                self.isInstalled = self.exists(self.name)
                self.lastInstall = self.lastInstall() if self.isInstalled else "Nao foi possivel recuperar data"
                self.lastUpdate = self.lastUpdate()
                self.isUpToDate = type(self.lastInstall) != str and self.lastInstall >= self.lastUpdate
            Tool.toolNum += 1
        else:
            Tool.num += 1

    def getDescription(self):  # Returns tool description
        d = get('https://api.github.com/repos' + self.url[18:] + '?access_token=' + Tool.access_token).json()[
            'description']
        return 'No description!' if d is None else d

    def lastUpdate(self):  # Returns last update for the tool on GitHub
        u = get('https://api.github.com/repos' + self.url[18:] + '?access_token=' + Tool.access_token).json()[
            'pushed_at']
        return self.strpTime(str(u.replace('T', ' ')[:-1]))

    def lastInstall(self):  # Returns last installation for the tool on PC
        if self.exists(self.name + '/install'):
            return self.strpTime(open(self.name + '/install', 'r').read())
        else:
            return "Nao foi possivel recuperar data"

    def clone(self, *path):  # Clone the tool to the path argument
        print(f'Instalando: {self.name} : ', )
        if not os.system('git clone -q ' + self.url + ' ' + ('/tmp/' if path else '') + self.name):
            print(green + 'Ok' + end)
            open(('/tmp/' if path else '') + self.name + '/install', 'w').write(Tool.strfTime(datetime.now()))
        else:
            print(f'{red} Error {end}')

    def remove(self, *path):  # Delete the passed directory
        if Tool.exists(('/tmp/' if path else '' + self.name)):
            if path:
                print('Excluindo ferramenta de /tmp/ : ', )
            else:
                print('Deleting the previous version of ' + self.name + ': ', )
            if not os.system('rm -rf ' + ('/tmp/' if path else '') + self.name):
                print(green + 'Ok' + end)
            else:
                print(red + 'Error' + end)

    def copy(self):  # Copy installed tool from tmp to current directory
        print('Copying the tool : ', )
        if not os.system('cp -af /tmp/' + self.name + ' ./'):
            print(green + 'Ok' + end)
        else:
            print(red + 'Error' + end)

    def printInfo(self):  # Print some information about found tools
        print('Tool Number: ' + red + str(self.num) + end)
        print('Tool: ' + red + self.name + end)
        print('Author: ' + red + self.author + end)
        print('URL: ' + red + self.url + end)
        print('Availability: ' + ((green + 'Available') if self.available else (red + 'Not available')) + end)
        if self.available:
            print('Description: ' + red + self.desc + end)
        if hasattr(self, 'isInstalled'):
            print('Last Update On GitHub: ' + red + Tool.strfTime(self.lastUpdate) + end)
            print('Last Update On PC: ' + red + (
                self.lastInstall if type(self.lastInstall) == str else Tool.strfTime(self.lastInstall)) + end)
            print('Uptodate: ' + (green if self.isUpToDate else red) + str(self.isUpToDate) + end)
            print('Status: ' + (green + 'Instalada' if self.isInstalled else red + 'Nao intalada') + end)
        print(red + '================================================================================' + end)

    @staticmethod
    def getUrl(url):
        url = search('https:\/\/github\.com(\/\w+([-._]?\w*)+){2}', url.lower())
        if url:
            url = str(url.group())
            for x in ['.git', '/']: url = url[:None if not url.endswith(x) else -len(x)]
            return url

    @staticmethod
    def exists(path):  # Check if path exists or not
        return os.path.exists(path)

    @staticmethod
    def deleteFile(path):  # Delete the past path
        if Tool.exists(path):
            os.remove(path)

    @staticmethod
    def check(url):  # Checks that the tool is available on GitHub
        return get(f'https://api.github.com/repos {url[18:]}?access_token= {Tool.access_token}').ok

    @staticmethod
    def strpTime(date):  # Converts string to datetime object
        return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def strfTime(date):  # Converts datetime object to formated string
        return datetime.strftime(date, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def add(url):  # Add tool using URL
        try:
            url = Tool.getUrl(url)
            resource.write(url + '\n')
            print(f'{green} Nova ferramenta foi adicionada! :) {end}')
        except Exception as err:
            print(red + str(err) + end)

    @staticmethod
    def find(tool, t):  # Search for a tool on GitHub
        if t == 1:  # Cl0neMast3r
            req = get(params="Authorization:token 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",
                      url=f"https://api.github.com/search/repositories?q={tool}")
            print(req.text)
        else:
            req = get(params="Authorization:token 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",
                      url=f"https://api.github.com/users/{tool}")
            print(req)
        js = req.json()
        if req.ok:
            foundTools = []
            try:
                numOfTools = int(input(
                    'Eu encontrei {0}{1}{2} tools, Quantas ferramentas você quer que eu exiba {0}:{2} '.format(red, str(
                        (js['total_count'] if t == 1 else len(js))), end)))
            except NameError:
                print(f'{red}Algo de Errado! {end}')
                return
            j = js['items'] if t == 1 else js
            print(j[:numOfTools])
            for t in j[:numOfTools]:  # Shows the found tools in the found pages
                foundTools.append(t['html_url'])
                Tool(foundTools[-1]).printInfo()
            try:
                choice = int(input('Escolha uma opacao {0}:{1} '.format(red, end)))
            except NameError:
                print(f'{red}Algo de Errado! {end}')
                return
            if choice <= len(foundTools):
                wait()
                Tool.add(foundTools[int(choice) - 1])
            else:
                print(f'{red} Escolha um numero de 1 para {str(len(foundTools))} {end}')

    # --------------
    # Class Methods
    # --------------
    @classmethod
    def reset(cls):  # Reset tools' number
        cls.toolNum = cls.num = 1

    @classmethod
    def found(cls, toolURL):  # Check if the tool was added before
        return toolURL in [tool.url for tool in cls.list]

    @classmethod
    def display(cls):  # Display users tools
        if len(cls.list) == 0:  # Checks if the list is empty or not
            print(f'{red} Nenhuma ferramenta foi adicionada {end}')
        else:
            for tool in cls.list:
                tool.printInfo()

    @classmethod
    def update(cls):  # Update all tools on the list
        try:
            print('[{0}1{1}] Update todas suas ferramentas\n[{0}2{1}] Update suas ferramentas velhas'.format(red, end))
            x = int(input('Escolha 1 ou 2{0}:{1} '.format(red, end)))
        except NameError:
            print(f'{red} Algo de Errado! {end}')
            return
        if x == 1:
            listToUpdate = cls.list
        elif x == 2:
            listToUpdate = [tool for tool in cls.list if tool.available and not tool.isUpToDate]
        else:
            print(f'{red} Algo de Errado! {end}')
            return
        for tool in listToUpdate:
            print(green + '\n[' + tool.name + ']' + end)
            tool.remove('/tmp/')
            tool.clone('/tmp/')
            tool.copy()
            tool.remove('/tmp/')
            print(red + f'================================================ {end}')
            print(f'{green}\nSuas ferramentas ja estao atualizadas :) {end}')

    @classmethod
    def reinstall(cls):  # Reinstall all tools on the list
        for tool in cls.list:
            print(f'\n[ {tool.name} ]{end}')
            tool.remove()
            tool.clone()
            print(f'{red}================================================{end}')
        print(f'\n{green}Todas ferramentas reinstaladas!{end}')

    @classmethod
    def importToolsHtml(cls):  # Import tools from HTML page
        if cls.exists(cls.htmlFile):
            for tool in BeautifulSoup(open(cls.htmlFile, 'r').read(), 'html.parser').find_all('a'):
                cls.add(tool['href'])

    @classmethod
    def importToolsDir(cls):  # Import tools from current directory
        directories = [d for d in os.listdir('./') if os.path.isdir(d) and cls.exists(d + '/.git/config')]
        for d in directories:
            x = search('https://github.com/.+\w+', open(d + '/.git/config').read())
            if x:
                cls.add(x.group())

    @classmethod
    def exportTools(cls):  # Export tools on the list to HTML page
        Tool.deleteFile(cls.htmlFile)
        #   Beginning
        htmlCode = """<html><head><title>Cl0neMast3r</title><style>@font-face{font-family:Hacked;src:url(https://hackedfont.com/HACKED.ttf);}
body{color:red;background-color:black;text-align:center;font-size:25px;font-family:Hacked}
h1{font-size:55px;}a{display:block;width:200px;color:white;background-color:red;text-decoration: none;
border: 1px solid red;border-radius:10px;margin:20px auto;padding:5px;}</style></head><body><h1>Cl0neMast3r</h1>"""

        # Middle
        htmlCode += "".join(["<a href=" + tool.url + ">" + tool.name + "</a>" for tool in cls.list])

        # End
        htmlCode += "./Abdulraheem_Khaled</body></html>"
        soup = BeautifulSoup(htmlCode, 'html.parser')
        open(cls.htmlFile, 'w').write(soup.prettify())
        print(f'Ferramentas exportadas para: {red}{cls.htmlFile}{end}')


def wait():  # Wait until all tools on the list are updated
    if not updated:
        print(f'{red}Aguarde ate atualizar a suas lista de ferramentas{end}')
    while not updated:
        pass


def update():  # Update the list of tools
    global updated
    Tool.list = [Tool(tool, True) for tool in set([Tool.getUrl(tool.strip()) for tool in resource])]
    updated = True


while True:
    Tool.reset()  # Reset number of tools
    resource = open(Tool.toolsFile, 'a+')  # List of added tools
    resource.seek(0)  # Start reading from the beginning of file
    updated = False  # Check that tools list has been read
    Thread(target=update).start()  # Using threading to
    os.system('clear')
    print("""{0}
================================================================================
   _____ _  ___             __  __           _   ____
  / ____| |/ _ \           |  \/  |         | | |___ \\
 | |    | | | | |_ __   ___| \  / | __ _ ___| |_  __) |_ __
 | |    | | | | | '_ \ / _ \ |\/| |/ _` / __| __||__ <| '__|
 | |____| | |_| | | | |  __/ |  | | (_| \__ \ |_ ___) | |
  \_____|_|\___/|_| |_|\___|_|  |_|\__,_|___/\__|____/|_|

                ./{1}Abdulraheem Khaled {0}@{1}Abdulrah33mK{0}
================================================================================{2}
[{0}A{2}] Adiciona a ferramenta usando a URL
[{0}F{2}] Procura a ferramenta no GitHub 
[{0}R{2}] Reinstala suas ferramentas 
[{0}U{2}] Atualiza suas ferramentas
[{0}S{2}] Exibe suas ferramentas
[{0}D{2}] Deleta suas ferramentas
[{0}X{2}] Exporta suas ferramentas em HTML
[{0}M{2}] Importa todas suas ferramentas
[{0}E{2}] Exit """.format(red, white, end))
    choice = input('Como posso ajuda-lo: ' + red + ': ' + end).lower()
    # ---------------------------------------------------------------------------------
    if choice == 'a':
        print('[' + red + "Adicionando as suas ferramentas" + end + ']')
        r = "y"  # Add more tools
        while r == "y":
          wait()
          list = ['','','','','','','','','','','','','','','','','','','','','',]
          Tool.add(.lower())
          r = input("Quer adicionar outra ferramenta ? ({0}Y{1} or {0}N{1}): ".format(red, end)).lower()
    # ---------------------------------------------------------------------------------
    elif choice == 's':
        print(f'[{red}Exibindo Suas Ferramentas {end}]')
        wait()
        Tool.display()
    # ---------------------------------------------------------------------------------
    elif choice == 'r':
        print(f'[{red}Reinstalando suas Ferramentas. Favor Aguarde! {end}]')
        wait()
        Tool.reinstall()
    # ---------------------------------------------------------------------------------
    elif choice == 'u':
        print(f'[{red}Atualizando suas ferramnetaas{end}]')
        wait()
        Tool.update()
    # ---------------------------------------------------------------------------------
    elif choice == 'f':
        print(f'[{red}Procurar ferramenta{end}]')
        print(
            '[{0}1{1}] Pesquise usando o nome da ferramenta\n[{0}2{1}] Pesquise usando o username do usuario'.format(
                red, end))
        try:
            choice = int(input('Escolha {0}:{1} '.format(red, end)))
        except NameError:
            choice = 3
        if choice == 1 or choice == 2:
            Tool.find(input(f'Digite o nome para pesquisar {red} : {end}'), choice)
        else:
            print(f'{red}Algo de Errado! {end}')
    # ---------------------------------------------------------------------------------
    elif choice == 'd':
        print(f'[{red}Deletando suas Ferramentas tool {end}]')
        wait()
        Tool.deleteFile(Tool.toolsFile)
        print(f'{green}Ferramentas Deletadas {end}')
    # ---------------------------------------------------------------------------------
    elif choice == 'm':  # Importing your tools
        print(f'[{red} Importando as suas ferramentas {end}]')
        wait()
        print(
            'Escolha uma opcao{0}:{1}\n[{0}1{1}] Importe para HTML\n[{0}2{1}] Importe para seu diretorio atual'.format(
                red, end))
        try:
            choice = int(input('Informe uma opcao {0}:{1} '.format(red, end)))
        except NameError:
            choice = 3
        if choice == 1:  # HTML
            Tool.importToolsHtml()
        elif choice == 2:  # Current directory
            Tool.importToolsDir()
        else:
            print(f'{red}Algo de Errado! {end}')
    # ---------------------------------------------------------------------------------
    elif choice == 'x':  # Exporting your tools
        print(f'[{red} Exportando suas tool para HTML {end}]')
        wait()
        Tool.exportTools()
    # ---------------------------------------------------------------------------------
    elif choice == 'e':  # Exit
        print(f'{red}Saindooo .__. ..., Good Bye :D {end}')
        menu()
        break
    # ---------------------------------------------------------------------------------
    else:
        print(f'{red}Algo de Errado! {end}')
    # ---------------------------------------------------------------------------------
    while input('Enter {0}M{1} para voltar a pagina inicial: '.format(red, end)).lower() != 'm':
        print(f'{red}Algo de Errado! {end}')
