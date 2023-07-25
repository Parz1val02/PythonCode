#!/usr/bin/python3
import socket
import sys
import ipaddress

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <ip address> " + " <port number>")
    sys.exit(1)

#addr = ipaddress.ip_address(sys.argv[1])

sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_.connect((str(sys.argv[1]),int(sys.argv[2])))

message = sock_.recv(1024)#Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by (number).
sock_.close()
print(message.decode("ascii"))