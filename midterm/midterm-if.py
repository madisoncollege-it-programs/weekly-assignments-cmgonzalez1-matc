#!/usr/bin/env python3
#Midterm Activity 1: Flow Control
print("Name: Christian Gonzalez")

#Creating variable named "total".
total = 0

#Opening Midterm-if.txt for one time use (reading only)
with open("Midterm-if.txt" , 'r') as hFile:
    for line in hFile:
#Looks for gmeach18@ed.gov | convert to int | id = 45 | add into total
     if "gmeach18@ed.gov" in line:
            id = int(line[0:2])
            total += (id)
#Looks for 248.253.63.149 | convert to int | id = 345 | add into total
     if "248.253.63.149" in line:
            id = int(line[0:3])
            total += (id)
#Looks for Whiteland | convert to int | id = 11 | add into total
     if "Whiteland" in line:
            id = int(line[0:2])
            total += (id)
#Looks for 80.222.19.190 | convert to int | id = 530 | add into total
     if "80.222.19.190" in line:
            id = int(line[0:3])
            total += (id)
#Looks for Kayley | convert to int | id = 525 | add into total
     if "Kayley" in line:
            id = int(line[0:3])
            total += (id)
#Looks for dcassyqw@microsoft.com | convert to int | id = 525 | add into total
     if "dcassyqw@microsoft.com" in line:
            id = int(line[0:3])
            total += (id)
#Print out the total variable.
print(f"The total is: {total}")
