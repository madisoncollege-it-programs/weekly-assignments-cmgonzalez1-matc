#!/usr/bin/env python3
#Midterm Activity 3: Slicing
#Christian Gonzalez

#Opening to use throughout a script
hFile = open("slicing-file.txt","r")
str = hFile.read()

#The thrid word from the end of the list (Whether)
a = (str[126:133])

#The third through fith word of the list (you think you)
b = (str[16:29])

#The 10th word from the end of the file and every opther word for a total of 3
c = (str[92:95])
c1 = (str[84:86])
c2 = (str[74:77])
#The 11th through 13th word
d = (str[57:73])
#The 19th - 21 words from the end of the file
string = (str[36:50])
words = string.split()
e  = list(reversed(words))

#print words
print( a + '\n' + b + '\n' + c + '\n' + c1 + '\n' + c2 + '\n' + d)
print(" " .join(e))
