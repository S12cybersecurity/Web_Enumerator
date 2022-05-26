import argparse
import sys
import requests
from threading import Thread
import multiprocessing
import asyncio
import random


parser = argparse.ArgumentParser(description="Python Bruteforce Login")
parser.add_argument('--url', help="Website to target", required=True)
parser.add_argument('--extension', help="Extensions to find files (Ex: exe) Default .php", required=False)
parser.add_argument('--wordlist', help="Wordlist of passwords to use", required=True)
args = parser.parse_args()


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR

proxy = {
  'http': 'http://127.0.0.1:8080',
}

user_agent_list = [
'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2'
'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16'
'Opera/9.80 (Macintosh; Intel Mac OS X 10.14.1) Presto/2.12.388 Version/12.16'
'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'
'Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14'
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14'
'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02'
'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00'
'Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00'
'Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00'
'Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.1 (KHTML, like Gecko) Safari/125'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-ch) AppleWebKit/312.1.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-ca) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.1 (KHTML, like Gecko)'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.1.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/312.1.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312.3.1'
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577'
'Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931'
'Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
]

def directories(WORDLIST_FILENAME):
       global line
       wordlist = list()
       with open(WORDLIST_FILENAME) as f:
            for line in f:
                my_str=line.strip()
                user_agent = random.choice(user_agent_list)
                headers = {"User-Agent": user_agent}
                uuuuu = final_url+"/"+my_str
                uuuuu2 = final_url+"/"+my_str+"."+extensionn
                lista = list()
                ttt = requests.get(uuuuu,proxies=False,headers=headers)
                ttt2 = requests.get(uuuuu2,proxies=False,headers=headers)
                if ttt.status_code == 200:
                    delete = requests.delete(uuuuu)
                    get = requests.get(uuuuu)
                    post = requests.post(uuuuu)
                    head = requests.head(uuuuu)
                    put = requests.put(uuuuu,proxies=False)
                    patch = requests.patch(uuuuu)
                    if get.status_code == 200:
                        lista.append("GET")
                        if post.status_code == 200:
                            lista.append("POST")
                            if delete.status_code == 200:
                                lista.append("DELETE")
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista) 
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                else:
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)

                            else:
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                else:
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)


                        else:
                            if delete.status_code == 200:
                                lista.append("DELETE")
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                
                        

                                    

                            else:
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                else:
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)

                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)


                            
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                    
                                else:
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                           

                    else:
                        if post.status_code == 200:
                            lista.append("POST")
                            if delete.status_code == 200:
                                lista.append("DELETE")
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)

                                else:
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                    

                            else:
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                        else:
                            if delete.status_code == 200:
                                lista.append("DELETE")
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                else:
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
     
                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista) 
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
        

                            else:
                                if head.status_code == 200:
                                    lista.append("HEAD")
                                    if put.status_code == 200:
                                        lista.append("PUT")
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)


                                    else:
                                        if patch.status_code == 200:
                                            lista.append("PATCH")
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                        else:
                                            print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu,f"{bcolors.OK}- HTTP VERBS ACCEPTED:{bcolors.RESET}",lista)
                                

                elif ttt.status_code == 404:
                    pass
                else:
                    pass
                if ttt2.status_code == 200:
                    print(f"{bcolors.OK}[+] Status Code 200: {bcolors.RESET}",uuuuu2)
                elif ttt2.status_code == 404:
                    pass
                else:
                    pass
                
global test

try:
    test = requests.get(args.url)
    print(f"{bcolors.WARNING}[+] CONNECTING WITH TARGET{bcolors.RESET}")
except ConnectionRefusedError():
    print(f"{bcolors.FAIL}[+] CONNECTION REFUSED{bcolors.RESET}")



if args.url[-1] == "/":
    final_url = args.url[:-1]
else:
    final_url = args.url 

if args.extension == None:
	extensionn = "php"
else:
	extensionn = args.extension

directories(args.wordlist)