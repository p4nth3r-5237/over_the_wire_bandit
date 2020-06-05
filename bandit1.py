#!/usr/bin/python3

from pwn import *
import subprocess
flag0=str(subprocess.check_output('cat flag.txt | cut -d " " -f 3', shell=True).strip())[2:-1]


s = ssh(user="bandit1", host="bandit.labs.overthewire.org", port=2220, password=flag0)
flag1=str(s.process("cat ./-", shell=True).recvall().strip())[2:-1]

print(f"password for bandit2 --> {flag1}")
with open("flag.txt", "a") as f:
	f.write(f"bandit1 --> {flag1}\n")