# EncDec
Simple Python scripts to encrypt and decrypt files

----
### Installation

Just clone the repository and run the scripts. 

```
git clone https://github.com/julio-cfa/EncDec.git
```

There are 2 requirements: the colorama and cryptography libraries. You can install them with pip (pip install colorama && pip install cryptography). It is quite simple.

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


Feel free to change the scripts and adapt it to suit you better.
