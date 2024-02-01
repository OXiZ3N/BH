# -*-coding:Latin-1 -*
import sys
from requests import get
from colorama import Fore, init
import random
from fake_headers import Headers
import ctypes
from re import findall
from multiprocessing.dummy import Pool
import os

os.system('cls' if os.name == 'nt' else 'clear')
if os.name == 'nt':
    ctypes.windll.kernel32.SetConsoleTitleW('Private Reverse IP By OXiZ3N')
else:
    sys.stdout.write('Private Reverse IP By OXiZ3N')  

init(autoreset=True)
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA

header = Headers(browser='chrom', os='win', headers=True)

def process_ip(ip):
    api1(ip)
    api2(ip)

def api1(ip):
    try:
        url = 'https://api.webscan.cc/?action=query&ip=' + ip
        send_data = get(headers=header.generate(), url=url, timeout=15).text
        getlist = findall('"domain": "(.*?)",', send_data)[3:]
        with open('Results.txt', 'a') as revip1_file:
            for domain in getlist:
                domain_lower = domain.lower()
                if "result" not in domain_lower and "total" not in domain_lower:
                    if not domain_lower.startswith("webmail.") and not domain_lower.startswith("ftp.") and not domain_lower.startswith("cpanel.") and not domain_lower.startswith("webdisk.") and not domain_lower.startswith("cpcalendars.") and not domain_lower.startswith("mail.") and not domain_lower.startswith("cpcontacts.") and not domain_lower.startswith("ns1.") and not domain_lower.startswith("ns2."):
                        domain = domain.replace("www.", "")                          
                        print('\033[1;32m'+ip+' ---> '+ '\033[1;35m'+domain)
                        revip1_file.write(domain + '\n')
    except:
        pass  

def api2(ip):
    try:
        url = 'https://core.xreverselabs.my.id/?api_key=private1&ip=' + ip
        send_data = get(headers=header.generate(), url=url, timeout=15).text
        getlist = findall('"(.*?)"', send_data)[3:]
        
        with open('Results.txt', 'a') as revip_file:
            for domain in getlist:
                domain_lower = domain.lower()
                if "status" not in domain_lower and "success" not in domain_lower and "Domains" not in domain_lower:
                    if not domain_lower.startswith("webmail.") and not domain_lower.startswith ("ftp.")and not domain_lower.startswith ("cpanel.")and not domain_lower.startswith ("webdisk.")and not domain_lower.startswith ("cpcalendars.")and not domain_lower.startswith ("mail.")and not domain_lower.startswith ("cpcontacts.")and not domain_lower.startswith ("ns1.")and not domain_lower.startswith ("ns2."):
                        domain = domain.replace("www.", "") 
                        domain = domain.replace("Domains", "")                        
                        print('\033[1;32m'+ip+' ---> '+ '\033[1;35m'+domain)
                        revip_file.write(domain + '\n')
    except:
        pass  

def main():
    print(
        """
        [#] Create By ::

 ██████╗ ██╗  ██╗██╗███████╗██████╗ ███╗   ██╗    ██████╗ ███████╗██╗   ██╗
██╔═══██╗╚██╗██╔╝██║╚══███╔╝╚════██╗████╗  ██║    ██╔══██╗██╔════╝██║   ██║
██║   ██║ ╚███╔╝ ██║  ███╔╝  █████╔╝██╔██╗ ██║    ██████╔╝█████╗  ██║   ██║
██║   ██║ ██╔██╗ ██║ ███╔╝   ╚═══██╗██║╚██╗██║    ██╔══██╗██╔══╝  ╚██╗ ██╔╝
╚██████╔╝██╔╝ ██╗██║███████╗██████╔╝██║ ╚████║    ██║  ██║███████╗ ╚████╔╝ 
 ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚══════╝  ╚═══╝  
                                                                                                                                           
                        Private Reverse IP 2 Methods
                                                 
           """)
    ovain = input('Enter list IPs : ')
    poolAmount = int(input("Thread: "))
    opens = open(ovain, mode='r', errors='ignore').read().splitlines()
    Professor = Pool(poolAmount)
    Professor.map(process_ip, opens)

main()
input("Finished!:)")
