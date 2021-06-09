#!/usr/bin/env python3

#AUTHOR: H4ckr0pZ
#FOLLOW ME ON INSTAGRAM:-> https://instagram.com/_rough_life_rider_/

import os
from os import system


c ='clear'
r ='python3 mac_changer.py'
i ='python3 -m pip install subprocess.run'
h ='python3 mac_changer.py -h'

os.system(c)
print("[+] Installing Subprocess Module...")
os.system(i)
command =input("Do you want to run the tool now?[y/n]").lower()

if command == "y":
    os.system(c)
    os.system(r)

elif command == "yes":
    os.system(c)
    os.system(r)

elif command == "n":
    os.system(h)
    print("ok bye...")

elif command == "no":
    os.system(h)
    print("ok bye....")
else:
    print("i can't understand...")
    os.system(h)

