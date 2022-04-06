#!/usr/bin/env python3

#Create a function that will convert from degrees fahrenheit to celsius
def print_celsius():

    #Asks the user for a temperature  in degrees Fahrenheit
    fahrenheit = input("Enter the temperature in fahrenheit > ")
    #Formula
    celsius = (int(fahrenheit) - 32) * 5/9
    #Prints the result of the function
    print("Fahrenheit to Celsius is > ", celsius)

print_celsius()
