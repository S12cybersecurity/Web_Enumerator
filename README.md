# Web_Enumerator
Python Script to enumerate Direcories Files and the HTTP Methods to Acces to the Discovered Resources

**Installation**

git clone https://github.com/S12cybersecurity/Web_Enumerator

pip3 install requests

pip3 install asyncio

pip3 install threading

pip3 install argparse

**Usage**

- Basic Use:

python3 web_discover.py --url http://127.0.0.1 --wordlist wordlist.txt

![image](https://user-images.githubusercontent.com/79543461/170592081-d9a6772d-c3ec-4513-9a71-bb6bc20f1ec8.png)


- Searching different extensions:

python3 web_discover.py --url http://127.0.0.1 --wordlist wordlist.txt --extension js

[+] If you don't specify extension it will automatically search for files with php extensions :)

![image](https://user-images.githubusercontent.com/79543461/170592790-b9b17867-760b-4502-8e63-a425c3285760.png)

**Features**

In this script to discover resources, brute force is used, user-agents in constant rotation to avoid possible locks.

To discover HTTP methods just like in brute force, use the request library.
I can identify the allowed methods thanks to the fact that when a method is not allowed, the server responds with a code state 405.

Developed in python 3.10 :)

@s12
