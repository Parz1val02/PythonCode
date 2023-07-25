import socket

sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_.connect((socket.gethostname(),6666))

message = sock_.recv(1024)#Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by (number).
sock_.close()
print(message.decode("ascii"))