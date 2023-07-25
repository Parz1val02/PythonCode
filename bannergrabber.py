#!/usr/bin/python3
import socket
import sys
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <ip address> ")
    sys.exit(1)
    
Ports = [21,22,25,3306]
for i in range(0,4):
    sock_=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    Port = Ports[i]
    print(f"This is the banner for the port {Port}")
    sock_.connect((str(sys.argv[1]),Port))
    message = sock_.recv(1024)#Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by (number).
    sock_.close()
    print(message.decode("utf8"))