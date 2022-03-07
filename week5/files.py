#[Lab-Python] File Data Interactions

# 1) Open the "/etc/passwd" file using read only access and save the full file contents to a str data type
# (Note: you will need to select the correct read function read function to return a string).
pFile = open( "/etc/passwd","r")
strfiletext=pFile.read()
print("String Data:")
# A. Use the len() function to get the size and print it out to the screen.
print(f"The /etc/passwd/ file is {len(strfiletext)} bytes long")

# B. Add a print statement to your script to indicate what the len() fuction counts
print("The len() fuction counts the letters in the /etc/passwd/ file")

# C. Add a print statement to your script to describe when you use this read function over other read functions.
print("This function would be useful to read all characters of a file and store in a string")
print()
pFile.close()

# 2) Open the "/etc/passwd" file using read only access and save the full file contents to a list data type.
# (Note you will need to select the correct read function to return a list)
pFile = open("/etc/passwd","r")
listfiletext = pFile.readlines()
print("List Data:")
# A. Use the len() function to get the size and print it out to the screen.
print(f"The /etc/passwd/ file is {len(listfiletext)} bytes long")

# B. Add a print statement to you script to indicate what the len() fuction counts
print("The len() fuction counts each lines in the /etc/passwd/ file")

# C. Add a print statement to your script to describe when you would use this read function over when you'd use other read functions.
print ("This function would be useful to read all lines of a file and store in a list")
print()
pFile.close

# 3) Open the "/etc/passwd" file using read only access and save the full file contents one line at a time to a variable.
# (Note you will need to select the correct read function to return one line at a time and store it during each iteration of the loop)
with open("/etc/passwd","r") as pFile:
# A. Add code that will calculate the total length of the file (number of characters) and print it out to the screen.
    try:
        while True:
         current_line = next(pFile)
         print(f"This line is {len(current_line)} byes long") 
# B. Add a print statment to your script to describe when you would use this technique over another read function    
    except StopIteration:
        print(f"This read technique would be help to read larger files")

