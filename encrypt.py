#!/usr/bin/python3

from colorama import Fore, Style, Back

from cryptography.fernet import Fernet

print(Fore.YELLOW + '''
          .-""-.
         / .--. \\
        / /    \\ \\
        | |    | |
        | |.-""-.|
       ///`.::::.`\\
      ||| ::/  \\:: ;
      ||; ::\__/:: ;
       \\\ '::::'  /
        `=':-..-'`
          
          LeT's
          EncRyPt
''' + Style.RESET_ALL)

filekey_raw = input(Fore.CYAN + "Where is your key?\n" + Style.RESET_ALL)
with open(filekey_raw, 'rb') as filekey:
    key = filekey.read()
  
fernet = Fernet(key)
  
fileraw = input(Fore.CYAN + "\nWhat file do you want to encrypt?\n" + Style.RESET_ALL)
with open(fileraw, 'rb') as file:
    original = file.read()
      
encrypted = fernet.encrypt(original)
  
with open(fileraw, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

print('\nYour file has been successfully ' + Fore.YELLOW + 'encrypted' + Style.RESET_ALL + '!')
