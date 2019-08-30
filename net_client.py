import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect()

addr = ("1.2.3.4", 24611)

sock.connect(addr)

user = input()
while(user.lower() != "n"):
	sock.sendall(user)
	sock.recv()
