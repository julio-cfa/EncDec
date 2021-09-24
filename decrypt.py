#!/usr/bin/python3

from colorama import Fore, Back, Style
from cryptography.fernet import Fernet

print(Fore.CYAN + '''

      .--.
     /.-. '----------.
     \\'-' .--"--""-"-'
      '--'
           LeT's
           DeCryPt

''' + Style.RESET_ALL)

filekey_raw = input(Fore.YELLOW + "Where is your key?\n" + Style.RESET_ALL)
fileraw = input(Fore.YELLOW + "\nWhat file do you want to decrypt?\n" + Style.RESET_ALL)

with open(filekey_raw, 'r') as filekey:
    key = filekey.read()
    fernet = Fernet(key)

with open(fileraw, 'rb') as enc_file:
    encrypted = enc_file.read()

decrypted = fernet.decrypt(encrypted)

with open(fileraw, 'wb') as dec_file:
    dec_file.write(decrypted)

print('\nYour file has been successfully ' + Fore.CYAN + 'decrypted' + Style.RESET_ALL + '!')
