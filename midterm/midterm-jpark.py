#!/usr/bin/env python3
#Midterm Activity 2: A Python In Jurassic Park
#Christian Gonzalez

print("Name: Christian Gonzalez")

#Creating a password_database
password_database = {'Username':'dnedry', 'Password': 'please'}
#Creating a command_database
command_database = {'reboot':' OK. I will reboot all systems.','shutdown':' OK. I will shut down all park systems.','done':' I hate all this hacker stuff.'}
#Initialize two objects name white_rabbit_object and counter
white_rabbit_object = 0
counter = 0

#Create a while loop:
while True:
    input_user = input("Username > " )
    input_password = input("Password > " ) 
#IF statement to compare the user input against the values
    if (input_user == password_database['Username']) and (input_password == password_database['Password']):
        white_rabbit_object = 1
        print("===" * 30)
        print("Hi, Dennis. You're still the best hacker in Jurassic Park.")
#Ask the user to enter a command
        input_command = input(f"Please enter a command:\n{command_database.keys()} > ")
#Evaluate the command provided by the user
        if input_command == 'reboot':
            print(command_database['reboot'])
            break
        elif input_command == 'shutdown':
            print(command_database['shutdown'])
            break
        elif input_command == 'done':
            print(command_database['done'])
            break
        else:
            print("The Lysine Contingency has been put into effect.")
            break
#Otherwise, if either the input are incorrect
    else:
        counter += 1
        if counter == 3:
            print("You didn't say the magic word.\n" * 25)
            break
