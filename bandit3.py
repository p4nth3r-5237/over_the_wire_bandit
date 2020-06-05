from pwn import *
import sys

try:
	try:
		flag3=sys.argv[1]
	except:
		print("[!!] Password need to login as args")
	s=ssh(user="bandit3", host="bandit.labs.overthewire.org", password=flag3, port=2220)
	print(flag3)
	flag4=str(s.process('cat inhere/.hidden', shell=True).recvall().strip())[2:-1]

	print(f"password for bandit4 --> {flag4}")
	with open("flag.txt", "a") as f:
		f.write(f"bandit3 --> {flag4}\n")
except:
	print("[!!] Error, Try previous challenge first or check internet")