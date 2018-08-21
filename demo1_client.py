# demo1_client.py
# purpose: simple client/server example, this is a client program
# date : august 21st /2018
# the server for this is demo2_server.py


import socket
import sys


# Create TCP/IP socket socket.AF_INET = Ipv4 connection
stream_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# define  host
host = 'localhost'
# define communication port 
port = 8080

# connect the socket to that port where the server is listening
server_address = ((host,port))

# print message
print("connecting to server at ...",server_address)

stream_socket.connect(server_address)

print("sending data...")
# send data 
message = 'user_id=224' # for unique address identification
stream_socket.sendall(message)


# response 
data = stream_socket.recv(10)
print("received data =",data)

print("closing socket")
stream_socket.close()
