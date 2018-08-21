# demo3_server.py
# purpose: simple server program in python to know network programming
# date : august 21st /2018
# the client for this is demo3_client


import socket
import sys
# import time

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define host
host = 'localhost'

# define communication port
port = 8080

# bind the socket to that port
sock.bind((host, port))

# Listen for incomming connections
sock.listen(1)

# waiting for a connection
print("waiting for a connection to a client...")

connection, client = sock.accept()

# connection successful
print("\nconnection successful... to", client)

# time.sleep(3)

# receive the data in small chunks and retransmit it
print("\nreveive data from client...")
data = connection.recv(16)

print('\nreceived "%s"' % data)
data2 = b'Ack:data receive successful!'
if data:
    connection.sendall(data2)
else:
    print("no data from ", client)

# close the connection
print("\nclosing connection....")
connection.close()
