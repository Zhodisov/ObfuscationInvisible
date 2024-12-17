import importlib.metadata
import subprocess
import sys

def i():
    try:
        if getattr(sys, 'frozen', False):
            return

        required_packages = ['requests', 'colorama', 'pystyle', 'pycryptodome', 'rich']
        installed_packages = {pkg.metadata['Name'].lower() for pkg in importlib.metadata.distributions()}
        missing_packages = [pkg for pkg in required_packages if pkg not in installed_packages]

        if missing_packages:
            for package in missing_packages:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except Exception:
        print("Ошибка установки пакетов")

import os

i()
import requests
import uuid
from colorama import init, Fore, Back, Style
import time
import threading
import socket
from rich.console import Console
from rich.table import Table
from rich.text import Text
import platform

init(autoreset=True)
console = Console()

APPDATA_PATH = os.getenv('APPDATA')
SAFEMARKET_FOLDER = os.path.join(APPDATA_PATH, 'safemarket')
KEY_STORAGE_FILE = os.path.join(SAFEMARKET_FOLDER, '0000002.bin')


def git():
    github_url = "https://safemarket.xyz/endpoint"
    try:
        response = requests.get(github_url, timeout=10)
        response.raise_for_status() 
        return response.text.strip()
    except Exception:
        print(Fore.RED + "невозможно получить содержимое." + Fore.RESET)
        return None


API = git() or sys.exit(Fore.RED + "Невозможно получить содержимое.")
SERVER_URL = f"https://api-v1.safemarket.xyz{API}"

def ip():
    try:
        response = requests.get("https://httpbin.org/ip", timeout=5)
        response.raise_for_status()
        ip = response.json().get("origin")
        return ip
    except (requests.exceptions.RequestException, ValueError):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except socket.error:
            return "Неизвестный IP-адрес"

def t(title):
    os.system(f"title {title}")

def tp(title, delay=0.1):
    for i in range(len(title) + 1):
        t(title[:i])
        time.sleep(delay)

def vl():
    dsc(banner)
    ip = ip()
    try:
        response = requests.post(f"{SERVER_URL}/rizz", json={"ip": ip})
        if response.json().get('status') != "success":
            sys.exit(Fore.RED + "Неверный ключ" + Fore.RESET)
    except Exception:
        sys.exit(Fore.RED + "Ошибка проверки лицензии." + Fore.RESET)



def cl():
    os.system('cls' if os.name == 'nt' else 'clear')
from pystyle import System, Anime, Colors, Colorate, Center
text = r"""
     /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$      /$$  /$$$$$$  /$$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$$
    /$$__  $$ /$$__  $$| $$_____/| $$_____/| $$$    /$$$ /$$__  $$| $$__  $$| $$  /$$/| $$_____/|__  $$__/
   | $$  \__/| $$  \ $$| $$      | $$      | $$$$  /$$$$| $$  \ $$| $$  \ $$| $$ /$$/ | $$         | $$   
   |  $$$$$$ | $$$$$$$$| $$$$$   | $$$$$   | $$ $$/$$ $$| $$$$$$$$| $$$$$$$/| $$$$$/  | $$$$$      | $$   
    \____  $$| $$__  $$| $$__/   | $$__/   | $$  $$$| $$| $$__  $$| $$__  $$| $$  $$  | $$__/      | $$   
    /$$  \ $$| $$  | $$| $$      | $$      | $$\  $ | $$| $$  | $$| $$  \ $$| $$\  $$ | $$         | $$   
   |  $$$$$$/| $$  | $$| $$      | $$$$$$$$| $$ \/  | $$| $$  | $$| $$  | $$| $$ \  $$| $$$$$$$$   | $$   
    \______/ |__/  |__/|__/      |________/|__/     |__/|__/  |__/|__/  |__/|__/  \__/|________/   |__/ 
                                        
                                        
                                                
                                                нажмите Enter...       
                                                
                                                  
               ┌──────────────────────────────────────────────────────────────────────────────┐
               │            Присоединяйтесь к Discord: www.safemarket.xyz/discord             │
               ├──────────────────────────────────────────────────────────────────────────────┤
               │                         Веб-сайт: www.safemarket.xyz                         │
               └──────────────────────────────────────────────────────────────────────────────┘
"""[:-1]

banner = """


     /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$      /$$  /$$$$$$  /$$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$$
    /$$__  $$ /$$__  $$| $$_____/| $$_____/| $$$    /$$$ /$$__  $$| $$__  $$| $$  /$$/| $$_____/|__  $$__/
   | $$  \__/| $$  \ $$| $$      | $$      | $$$$  /$$$$| $$  \ $$| $$  \ $$| $$ /$$/ | $$         | $$   
   |  $$$$$$ | $$$$$$$$| $$$$$   | $$$$$   | $$ $$/$$ $$| $$$$$$$$| $$$$$$$/| $$$$$/  | $$$$$      | $$   
    \____  $$| $$__  $$| $$__/   | $$__/   | $$  $$$| $$| $$__  $$| $$__  $$| $$  $$  | $$__/      | $$   
    /$$  \ $$| $$  | $$| $$      | $$      | $$\  $ | $$| $$  | $$| $$  \ $$| $$\  $$ | $$         | $$   
   |  $$$$$$/| $$  | $$| $$      | $$$$$$$$| $$ \/  | $$| $$  | $$| $$  | $$| $$ \  $$| $$$$$$$$   | $$   
    \______/ |__/  |__/|__/      |________/|__/     |__/|__/  |__/|__/  |__/|__/  \__/|________/   |__/ 
                                        
                                        
                                        
                                                
                                                нажмите Enter...       
                                                
                                                  
               ┌──────────────────────────────────────────────────────────────────────────────┐
               │            Присоединяйтесь к Discord: www.safemarket.xyz/discord             │
               ├──────────────────────────────────────────────────────────────────────────────┤
               │                         Веб-сайт: www.safemarket.xyz                         │
               └──────────────────────────────────────────────────────────────────────────────┘
"""[1:]


def dsc(banner):
    cl()
    Anime.Fade(Center.Center(banner), Colors.red_to_white, Colorate.Vertical, enter=True)
    

if __name__ == "__main__":
    System.Size(200, 40)
    tlthr = threading.Thread(target=tp, args=("www.safemarket.xyz - SafeMarket Obfuscation",))
    tlthr.start()
    lthr = threading.Thread(target=vl)
    lthr.start()
    lthr.join()
    cl()
