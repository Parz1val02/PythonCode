#!/usr/bin/python3
import socket
import sys

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <port number>")
    sys.exit(1)

host_name = socket.gethostname()#Gets the hostname where the python interpreter is running
IP_address = socket.gethostbyname(host_name)#Gets ip address of given host name
port = int(sys.argv[1])
sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET means ipv4 family, SOCK_STREAM means tcp connection
sock_.bind((IP_address,port)) #It takes only one element, hence the ()
sock_.listen(1) #Enables the server to recive connections, the number specifies the number of unaccepted connections that the system will allow before refusing new connections

print("\nServer started...\n")

conn,addr = sock_.accept() #Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.

print("Connection established with: ",str(addr))


message = "\nThank you for connecting "+str(addr)
conn.send(message.encode("ascii"))#Send data to the socket. The socket must be connected to a remote socket. Returns the number of bytes sent.
conn.close()
