#!/usr/bin/env  python3

#A function that will convert from degrees celsius to fahrenheit
def print_fahrenheit():
    #Asks the user for a temperature in degrees Celsius
    celsius = input("Enter the temerature in celsius > ")
    #Formula
    fahrenheit = (int(celsius) * 9/5) + 32
    #Prints the result of the function
    print("Celsius to Fahrenheit is > ", fahrenheit)

print_fahrenheit()
