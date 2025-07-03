from http import client
import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP/IP socket
s.bind(('127.0.0.1', 55555))  # Bind the socket to the address and port
s.listen() # Listen for incoming connections

while True:
    client, adress=s.accept()  # Accept a connection
    print("Connected to {}".format(adress))
    client.send("You are connected!".encode())  # Send a message to the client
    client.close()  # Close the connection


##CLIENT CODES 

import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
s.connect('127.0.0.1', 55555)  # Connect to the server
message=s.recv(1024)  # Receive data from the server
s.close()  # Close the socket

print(message.decode())  # Print the received message
