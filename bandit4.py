#!/usr/bin/python3

from pwn import *
import sys
try:
	try:
		flag4=sys.argv[1]
	except:
		print("[!!] Passwords need to login as args")	
	s=ssh(user="bandit4", host="bandit.labs.overthewire.org", password=flag4, port=2220)
	flag5=str(s.process('cat inhere/-file07', shell=True).recvall().strip())[2:-1]
	print(f"password for bandit5 --> {flag5}")
except:
	print("[!!] Error, Check internet")