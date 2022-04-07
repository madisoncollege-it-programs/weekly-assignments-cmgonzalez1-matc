#!/usr/bin/env python3

import subprocess

#Store the 'CompleatedProcess' return value in a variable name 'MyPorc'
myProc = subprocess.run(['ps','-axco','command'],stdout=subprocess.PIPE)

#Use decode() to extract the string data out of 'stdout'
#   Save this into a variable named 'myProcString'
myProcString = myProc.stdout.decode()

#Use split('\n') to create a list from your decoded data
#   Save this into a variable named 'myProcList'
myProcList = myProc.stdout.decode().split('\n')

#Planned to count the proccess as it is being printed
#Had to start with -1 so it will not count the command line
total = -1

#Use a for loop to print out all of the process name on line at a time
for line in myProcList[:-1]:
    total += 1 
    print(f"{total}: {line}") 
    print("------" * 7)

#Count the number of process in the list using the len() function
total = len(myProcList[1:][:-1])

#Print the count len() to the screen
print(f"Total of Process: {total}")
