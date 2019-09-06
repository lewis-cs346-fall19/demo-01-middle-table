#server file
import socket

def main():
    #create socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #returns name of local machine
    host = socket.gethostname()

    addr = (host, 24611)

    #binds socket to port 24611
    sock.bind(addr)

    #listen for connection, queue 5
    sock.listen(5)

    while True:
        #accept connection
        (connectedSock, clientAddress) = sock.accept()
        print("Connected with %s" % addr[0])
        msg = "Connected"
        connectedSock.send(msg.encode('utf-8'))
        try:
            while True:

                #receive message
                msg = connectedSock.recv(1024).decode()

                if not msg:
                    break

                else:
                    #reverse and return message
                    msg = msg[::-1]
                    connectedSock.sendall(msg.encode('utf-8'))
        except:
            sock.close()
        connectedSock.close()
        print("Connection with %s ended\n." % addr[0])
        
main()
		
