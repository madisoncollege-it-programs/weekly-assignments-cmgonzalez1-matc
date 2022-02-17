#Christian Gonzalez
#Purpose: Create a line or lines of python code that will output the format shown:

#Example:
#1. Output: 'Hello Timmy'
#2. Line of code in python script: 
#           print("Hello Timmy")

varString = "Here is a nice string to slice" 
varList = ["Here", "is", "a", "nice", "list", "to", "slice" ]
#Using slicing on VarString create the following output using one line of code:

#'e is a nice string to slice'
print(f"{varString[3:]}")

#'Her'
print(f"{varString[0:3]}")

#"e is a ni'
print(f"{varString[3:12]}")

#'Hr sanc tigt lc'
print(f"{varString[0::2]}")

#'ecils ot gnirts ecin a si ereH'
print(f"{varString[::-1]}")

print()
#Using slicing on varList create the following output using one line of code:

#['slice', 'to', 'list', 'nice', 'a', 'is', 'Here']
print(f"{varList[::-1]}")

#['a','is', 'Here']
print(f"{varList[2::-1]}")

#['a', 'nice']
print(f"{varList[0::3]}")

#['is', 'a', 'nice', 'list', 'to', 'slice']
print(f"{varList[1:]}")

print()
#Using a for loop, print out each element of varString one line at a time
for i in varString:
    print({i})

print()

for i in varList:
    print({i})

