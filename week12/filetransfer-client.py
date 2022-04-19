#!/usr/bin/env python3
import socket 

#Starting a TCP socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connecting to the server
s.connect((socket.gethostname(), 1234))

#Opening a nd reading the file data.
filename = input("What's the file name?: ")
file = open(f"{filename}", "r")

data = file.read()

#Sending the filename to the server.
s.send(f"{filename}".encode("utf-8"))

msg = s.recv(1024).decode("utf-8")

print(f"[SERVER]: {msg}")

#Sending the file data to the server
s.send(data.encode("utf-8"))
msg = s.recv(1024).decode("utf-8")
print(f"[SERVER]: {msg}")

#Writing data out to a new file
from os.path import exists
to_file = input("Which file do you want wish to send the text to? ")
print(f"Does the output file exist? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTRL-C to abort")
input()
 
in_file = open(filename)
indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)
print("DONE!")

out_file.close()
in_file.close()


#Closing
s.close()
