from pwn import *
import subprocess

flag1=str(subprocess.check_output('cat flag.txt | cut -d " " -f 3', shell=True)).split("\\n")[1]

s=ssh(user="bandit2", host="bandit.labs.overthewire.org", password=flag1, port=2220)
flag2=str(s.process('cat spaces\\ in\\ this\\ filename', shell=True).recvall().strip())[2:-1]
print(f"password for bandit3 --> {flag2}")
with open("flag.txt", "a") as f:
	f.write(f"bandit2 --> {flag2}\n")