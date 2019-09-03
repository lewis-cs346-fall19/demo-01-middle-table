#server file
import socket
def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	addr = ("0.0.0.0", 24611)
	sock.bind(addr)

	sock.listen(5)
	for i in range (5):
		print("boobobobobo")
		(connectedSock, clientAddress) = sock.accept()
	print(clientAddress)	

	try:
		msg = sock.recv(1024).decode()
	except:
		print("Something bad happened")
		sock.close()
	
	msg.append(msg[0] + "hello world")

	sock.sendall(msg.encode())

main()
		
