#!/usr/bin/env python3

import argparse
import sys
import requests,bs4
import json
import socket


# Create a new script that accepts two arguments
parser = argparse.ArgumentParser(description='Creating a parser to add arguments')

# A string argument with short flag of -i and a long flag of --ipaddress which accept an ip address. This should be required argument.
parser.add_argument('-i', '--ipaddress', required=True, dest='varAddress', type=str, help='Enter an IP address')

# A integer argument with a short flag of -f and a long flag of --function that takes in the unction number to call (1, 2, 3, 4, 5). This should be required argument.
parser.add_argument('-f', '--function', required =True, dest='varFunction', type=int, help='Enter a function number: 1-5')

# Checking for Arguments (Makes the arguments required)
if len(sys.argv) != 5:
    print(parser.print_help())
    exit(0)

# Using a formatted string, combine the IP address and the function number starting with ‘http://’ to create a URL.  Store this in a variable called URL. The URL format should look like: http://ipaddress/q#.  Replace ‘ipaddress’ with the ip address supplied by the user and the ‘#’ with the function number supplied by the user. 
URL = f"http://{(parser.parse_args()).varAddress}/q{(parser.parse_args()).varFunction}"

# Print out your first and last name.
print("Name: Christian Gonzalez")

# Print the URL
print(URL)

#=============== Function 1 ===============
# Create a function called 'get_response' that takes in the URL as an argument.
def get_response(URL):

    # Make a GET request to that URL
    response = requests.get(URL)

    # Return the text portion of the response
    print(f"ANSWER: {response.text}")

# Update your script to call this function when '1' is specified for the function number argument
if ((parser.parse_args()).varFunction == 1):
    get_response(URL)

#=============== Function 2 ===============
# Create a function called ‘parse_string’ that takes in the URL as an argument.  
def parse_string(URL):

    # Make a GET request to that URL
    response = requests.get(URL)

    # Use Beautiful Soup to print out contents of the H# element.
    response.raise_for_status()
    myHTML = bs4.BeautifulSoup(response.text,features="html.parser")
    H3 = myHTML.select('h3')

    #Return the sliced string with your first name appended to it. Use formatted strings too accomplish this.
    print(f"ANSWER: {str(H3)[9:27:2]} Christian")

# Update your script to call this function when '2' is specified for the function number argument.
if ((parser.parse_args()).varFunction == 2):
    parse_string(URL)

#=============== Function 3 ===============
#  Create a function called ‘parse_header’ that takes in the URL as an argument. 
def parse_header(URL):

    # Make a GET request to that URL
    response = requests.get(URL)

    # Find the MATC-HEADER from the response object.
    value = ([value for value in response.headers.values()][2])

    # Return this header value
    print(f"ANSWER: {value}")

# Update your script to call this function when '3' is specified for the function number argument
if ((parser.parse_args()).varFunction == 3):
    parse_header(URL)

#=============== Function 4 ===============
# Create a function called ‘parse_json’ that takes in the URL as an argument.  
def parse_json(URL):

    # Make a GET request to that URL
    response = requests.get(URL)

    # Loop through the 'Music And Books' values (which is JSON with multiple data types including a list
    json_dict = json.loads(response.text)
    test = (str(json_dict))
    # Return the publisher of the book titled The Shining
    print(f"ANSWER: {test[487:496]}")

# Update your script to call this function when '4' is specified for the function number argument.
if ((parser.parse_args()).varFunction == 4):
    parse_json(URL)

#=============== Function 5 ===============
# Create a function called ‘socket_client’ that takes in the ip address as an argument. 
IP = ((parser.parse_args()).varAddress)
def socket_client(IP):
    # Scan (make a connection) to the ports available on the server (ip address) in the range of [5000-6000].  Hint: You can use the range() function to step through a range of numbers.
    RHOST = IP
    RPORT = (range(5000,6000))
    mytimeout = 2

    for port in RPORT:

        C_SOCK = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        C_SOCK.settimeout(mytimeout)

        try:
            C_SOCK.connect((RHOST,port))
            #print(f"Connection State: {port}::The connection is successful")
            C_SOCK.send(bytearray("secret",'utf8'))
            RCV_DATA = C_SOCK.recv(1024)
            response = str(RCV_DATA)
            C_SOCK.close()
            print(f"ANSWER: {response[2:9:]}")
            break
        except socket.error as e:
            #print(f"Connection State: {port}::{e}")
            C_SOCK.close()
# Update your script to call this function when '5' is specified for the function number argument.
if ((parser.parse_args()).varFunction == 5):
    socket_client(IP)


