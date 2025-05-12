from os import system as c
import time
import random

G = '\033[1;32m'
R = '\033[1;31m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def clear(): c('clear')

def slow(text, speed=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def logo():
    clear()
    print(f"""{G} ▗▄▖▗▄▄▄▖▗▄▄▄▖▗▖ ▗▖    ▗▖  ▗▖ ▗▄▄▖
{G}▐▌ ▐▌ █    █  ▐▌▗▞▘     ▝▚▞▘ ▐▌   
{G}▐▛▀▜▌ █    █  ▐▛▚▖       ▐▌  ▐▌   
{G}▐▌ ▐▌ █  ▗▄█▄▖▐▌ ▐▌    ▗▞▘▝▚▖▝▚▄▄▖
------------------------------------
{G}[1] FREE FIRE DIAMOND HACK
[2] PASSWORD LIST
[0] EXIT
------------------------------------""")

def loading(text, dots=5, speed=0.3):
    print(text, end='')
    for _ in range(dots):
        print('.', end='', flush=True)
        time.sleep(speed)
    print()

def diamond_hack():
    clear()
    slow(f"{C}[*] CONNECTING TO GARENA FREE FIRE SERVER", 0.03)
    loading(f"{G}[*] SERVER STATUS")
    uid = input(f"{W}[?] ENTER FREE FIRE UID : {G}")
    slow(f"{W}[*] UID VERIFIED : {uid}", 0.03)
    loading(f"{G}[*] SELECTING DIAMOND PACKAGES")

    diamonds = [500, 1000, 5000, 10000, 50000]
    for d in diamonds:
        slow(f"{C}[+] INJECTING {d} DIAMONDS...", 0.05)
        time.sleep(0.5)

    loading(f"{Y}[!] FINALIZING TRANSACTION", 7, 0.2)
    slow(f"{G}[=] SECURITY VERIFICATION REQUIRED", 0.06)
    print(f"{G}VISIT : https://garena-vip-secure2025.com")
    input(f"\n{W}PRESS ENTER TO RETURN TO MENU...")
    menu()

def password_list():
    clear()
    slow(f"{G}VIP PASSWORD LIST", 0.05)
    print(f"{C}------------------------------")
    passwords = [
        'vipking2025', 'diamondinjector', 'freefiregod',
        'ffhack999', 'garena2025vip', 'prolegend', 'ffmastervip'
    ]
    for pw in passwords:
        slow(f"{W}- {pw}", 0.03)
    input(f"\n{W}PRESS ENTER TO RETURN TO MENU...")
    menu()

def menu():
    logo()
    choice = input(f"{G}[?] CHOICE : {G}")
    if choice == '1':
        diamond_hack()
    elif choice == '2':
        password_list()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION")
        time.sleep(1)
        menu()

menu()