#!/usr/bin/python3

from pwn import *
try:
	try:
		flag0=sys.argv[1]
	except:
		print("[!!] Password need to login as args")
	s=ssh(host="bandit.labs.overthewire.org", user="bandit0",password=flag0, port=2220)
	flag0=str(s.process('cat readme', shell=True).recvall().strip())[2:-1]
	print(f"password for bandit1 --> {flag0}")
	with open("flag.txt", "w") as f:
		f.write(f"bandit0 --> {flag0}\n")
except:
	print("[!!] Error, Try previous challenge first or check internet")