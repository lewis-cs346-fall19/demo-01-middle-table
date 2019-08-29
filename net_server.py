#server file

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	addr = ("1.2.3.4", 24611)
	sock.bind(addr)

	sock.listen(5)
	for i in range (1,101):
		(connectedSock, clientAddress) = sock.accept()
	
	try:
		msg = sock.recv(1024).decode()
	except:
		sock.close()
	
	msg.append(msg[0] + "hello world")

	sock.sendall(msg.encode())

main()
		
