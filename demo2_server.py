# demo2_server.py
# purpose: simple server program in python to know network programming
# date : august 21st /2018
# the client for this is demo1_client


import socket
import sys


# create TCP/IP socket 
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# define host
host = 'localhost'

# define communication port
port = 8080

# bind the socket to that port 
sock.bind((host,port))

# Listen for incomming connections
sock.listen(1)

# waiting for a connection
print("waiting for a connection...")

connection, client = sock.accept()

# connection successful
print("connection successful... to",client)


# receive the data in small chunks and retransmit it
print("reveive data...")
data = connection.recv(16)

print('received "%s"' %data)

if data:
    connection.sendall(data)
else:
    print("no data from ",client)

# close the connection
print("closing connection....")
connection.close()
