#!/usr/bin/env python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

#Server has accepted the connection from client
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
#Receiving the filename from client
    filename = clientsocket.recv(1024).decode("utf-8")

    print(f"[RECV] Receiving the filename data.")
    
    file = open(filename, "w")

    clientsocket.send(bytes("File data received","utf-8"))
#Receiving the data from the client
    data = clientsocket.recv(1024).decode("utf-8")
    print(f"[RECV] Receiving the file data")
    file.write(data)
    clientsocket.send(bytes("File data recevied","utf-8"))


#Closing the fie
    file.close()

clientsocket.close()
