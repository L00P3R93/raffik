#!/usr/bin/env python3

import sys
import platform

ver = platform.python_version()

if(ver <= '3'):
    print("\033[91m Raffik isn't compatible with python2 use python3.x\033[00m")
    sys.exit(1)

import random
import time
import os

try:
    from stem import Signal
    from stem.control import Controller
    import requests
except ImportError:
    print("\033[91m Install stem and requests with pip\033[00m")
    sys.exit(1)
print("""\033[91m

             __   __   _
            / _| / _| | |
 _ __  __ _| |_ | |_ _| | __ _
| '__|/ _` |  _||  _| | |/ /| |
| |  ( (_| | |  | | | |   < | |
|_|   \__,_|_|  |_| |_|_|\_\|_|\033[00m

				\033[93mv.1.0
				By sntaks\033[00m
""")

#tor_password = input("\033[92m Enter your tor password: \033[00m")

address = input("\033[92m Enter blog address: \033[00m")
views = int(input("\033[92m How many views you want: \033[00m"))

# signal Tor for new identity
def renew_connection():
    with Controller.from_port(address="127.0.0.1", port=9051) as controller:
        controller.authenticate() # found in /etc/tor/torrc file [HashedControlPassword]
        controller.signal(Signal.NEWNYM)
        controller.signal(Signal.HUP)
        time.sleep(5)

def tor_session():
    session = requests.session()
    session.proxies = {}
    session.proxies['http'] = 'socks5://localhost:9050'
    session.proxies['https'] = 'socks5://localhost:9050'
    return session

def visit():
    with open('agents.txt', 'r') as file:
        lines = open('agents.txt').read().splitlines()
    for num in range(views):
        header_value = random.choice(lines)
        header = {}
        header['User-Agent'] = header_value
        session = tor_session()
        session.get(address, headers=header) # visiting user URL
        print("\033[92m-\033[00m" * 150)
        print("\033[92m Page visited with the following ip with user-agent..\033[00m")
        print(session.get('http://httpbin.org/ip').text) # Display current IP
        print(session.get('http://httpbin.org/user-agent', headers=header)) # Display current User-Agent
        renew_connection()

        if num == (views - 1):
            print("\033[92m-\033[00m " * 150)
            print("\033[01m\033[93m successfully visited website ", views, " times\033[00m")
            sys.exit(0)

visit()