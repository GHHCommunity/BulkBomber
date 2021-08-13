import time
import pyautogui
from colorama import Fore
print(Fore.GREEN + ''' 
   GHHC Presents
------------------- ''' + Fore.RED + '''  


 ▄▄▄▄    █    ██  ██▓     ██ ▄█▀ ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
▓█████▄  ██  ▓██▒▓██▒     ██▄█▒ ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▓██  ▒██░▒██░    ▓███▄░ ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
▒██░█▀  ▓▓█  ░██░▒██░    ▓██ █▄ ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
░▓█  ▀█▓▒▒█████▓ ░██████▒▒██▒ █▄░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
░▒▓███▀▒░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ▒▒ ▓▒░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
▒░▒   ░ ░░▒░ ░ ░ ░ ░ ▒  ░░ ░▒ ▒░▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
 ░    ░  ░░░ ░ ░   ░ ░   ░ ░░ ░  ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ 
 ░         ░         ░  ░░  ░    ░          ░ ░         ░    ░         ░  ░   ░     
      ░                               ░                           ░ ''' + Fore.WHITE + ''' Created by R00tDev1l
        ''')
print("")
t = str(input(Fore.GREEN + "Enter texts: " + Fore.WHITE + ""))
y = int(input(Fore.GREEN + "Enter threads: " + Fore.WHITE + ""))
z = int(input(Fore.RED + "Enter timelimit: " + Fore.WHITE + ""))
print("")
print(Fore.WHITE + "All set and clear to go!!!")
print("")
input(Fore.GREEN + "Press enter to continue" + Fore.RED + "\nBut remember your time limit buddy!")
time.sleep(z)
i = 1
while i<=y:
    pyautogui.typewrite(t)
    pyautogui.press('enter')
    i = i + 1
