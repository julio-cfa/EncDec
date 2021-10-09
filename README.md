# EncDec
As I wanted to encrypt some .md and .txt files - especially since I use Obsidian and sometimes I have to save files that contain a certain level of confidentiality -, I've decided to built some simple Python scripts to encrypt and decrypt them. I haven't tested them in any extensions other than the aforementioned, so... Be careful with what kind of stuff you're encrypting. Back it up and test it before doing it for good.

----
### Installation

Just clone the repository and run the scripts. 

```
git clone https://github.com/julio-cfa/EncDec.git
```

There are 2 requirements: the colorama and cryptography libraries. You can install them with pip (pip install colorama && pip install cryptography). It is quite simple and straightforward.

----
### Keygen

```
$ python keygen.py 
What do you wanna call your filekey?
example.key

Your key was generated and you can find it inside the following file: example.key

```
----
### Encrypt

```
$ python encrypt.py 

          .-""-.
         / .--. \
        / /    \ \
        | |    | |
        | |.-""-.|
       ///`.::::.`\
      ||| ::/  \:: ;
      ||; ::\__/:: ;
       \\ '::::'  /
        `=':-..-'`
          
          LeT's
          EncRyPt

Where is your key?
example.key

What file do you want to encrypt?
example.file

Your file has been successfully encrypted!
```

----
### Decrypt

```
$ python decrypt.py 


      .--.
     /.-. '----------.
     \'-' .--"--""-"-'
      '--'
           LeT's
           DeCryPt


Where is your key?
example.key

What file do you want to decrypt?
example.file

Your file has been successfully decrypted!

```


Feel free to change the scripts and adapt it to suit your needs better.
