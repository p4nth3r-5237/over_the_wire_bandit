#!/usr/bin/python3

from pwn import *

l=listen()
s=ssh(host="bandit.labs.overthewire.org", user="bandit0",password="bandit0", port=2220)
print(str(s.process('cat readme', shell=True).recvall().strip())[2:-1])
