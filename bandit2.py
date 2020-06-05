from pwn import *
import subprocess

try:
	try:
		flag1=sys.argv[1]
	except:
		print("[!!] Password need to login as args")

	s=ssh(user="bandit2", host="bandit.labs.overthewire.org", password=flag1, port=2220)
	flag2=str(s.process('cat spaces\\ in\\ this\\ filename', shell=True).recvall().strip())[2:-1]
	print(f"password for bandit3 --> {flag2}")
	with open("flag.txt", "a") as f:
		f.write(f"bandit2 --> {flag2}\n")
except:
	print("[!!] Error, Try previous challenge first or check internet")