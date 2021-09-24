#!/usr/bin/python3

from cryptography.fernet import Fernet
from colorama import Style, Fore, Back

filename = input(Fore.CYAN + "What do you wanna call your filekey?\n" + Style.RESET_ALL)

key = Fernet.generate_key()

with open(filename, 'wb') as file:
    file.write(key)

print(f'\nYour key was generated and you can find it inside the following file: {filename}')

