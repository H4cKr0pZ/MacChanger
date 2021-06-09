#!/usr/bin/env python3

#AUTHOUR: H4ckr0pZ
#FOLLOW ME ON INSTAGRAM:-> https://instagram.com/_rough_life_rider_

import subprocess
import optparse
import time
from time import sleep


def get_argument():
    parser =optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="The interface to change the MAC")
    parser.add_option("-m","--mac",dest="new_mac",help="The NewMac address to apply")
    parser.parse_args()


def change_mac(interface,new_mac):
    print("[+] Changing the mac of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])
    print("Mac successfully changed to " + new_mac)

get_argument()
sleep(2)
print("use this tool with sudo [!]\n eg:sudo python3 mac_changer.py OR sudo python3 install.py")
print("""
----------------------------------------------------------------
|                MacChangeR BY H4ckr0pZ                        |
----------------------------------------------------------------
""")
interface =input("INTERFACE> ")
new_mac   =input("NEW_MAC>> ")
change_mac(interface,new_mac)
print("""
----------------------------------------------------------------
|                                                              |
----------------------------------------------------------------
""")





