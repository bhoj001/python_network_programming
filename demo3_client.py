# demo3_client.py
# purpose: simple client/server example, this is a client program, here we do some logic based on reveived data
# date : august 21st /2018
# the server for this is demo3_server.py


import socket
import sys
# import time  # this to make few seconds sleep

# Create TCP/IP socket socket.AF_INET = Ipv4 connection
stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define  host
host = 'localhost'
# define communication port
port = 8080

# connect the socket to that port where the server is listening
server_address = ((host, port))

# print message
print("connecting to server at...", server_address)

stream_socket.connect(server_address)

print("\nsending data to server from client...")
# send data
message = b'user_id=224'  # for unique address identification
stream_socket.sendall(message)

print("\nreceiving data from server...")
# time.sleep(5)
# response
data = stream_socket.recv(10)
print("\nreceived data =", data)
if data =="user_id=224":
    print("do some operation with user 224...")
else:
    print("no user present....")

print("\nclosing socket")
stream_socket.close()
