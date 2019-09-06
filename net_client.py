"""
    client file
"""

import socket

def main():

    #create socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #returns host name
    host = socket.gethostname()

    addr = (host, 24611)

    #connect to address
    sock.connect(addr)

    #accept message from server
    in_msg = sock.recv(1024)
    print(str(in_msg))

    #get user input
    user = input("Enter a string or '1' to quit: ")
    while(user.lower() != "1"):
        sock.sendall(user.encode('utf-8'))
        in_msg = str(sock.recv(1024))
        print(in_msg[2:])
        user = input("Enter a string or '1' to quit: ")
    sock.close()    
main()
