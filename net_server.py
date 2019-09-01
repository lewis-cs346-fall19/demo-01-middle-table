#server file
import socket
def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	addr = (host, 24611)
	sock.bind(addr)

	sock.listen(5)
	while True:
		connectedSock, clientAddress = sock.accept()
		print("Got a connection from %s" % str(addr))
		msg = 'Thank you for connecting'+ "\r\n"
		connectedSock.send(msg.encode('ascii'))
	sock.close()	
	
	# try:
	# 	msg = sock.recv(1024).decode()
	# except:
	# 	sock.close()
	
	# msg.append(msg[0] + "hello world")

	# sock.sendall(msg.encode())

main()
		
