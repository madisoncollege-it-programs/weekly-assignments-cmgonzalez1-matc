#!/usr/bin/env python3

import sys
import requests
import json
import argparse


#./my-json.py --{ipaddress}


#Turn an argument into a string
s = ' '.join(map(str, sys.argv))

#slice the argument to only get the ip address

ipaddress = s[15:]

# Create the url that we want to connect to
url = f"http://ipinfo.io/{ipaddress}/json"

# Send the "get" request to the web server
jsonResp = requests.get(url)
# Convert the reurned json formatted text to a dictionary 
dictResp = json.loads(jsonResp.text)

# for each key in the dictionary print the key and the data
for key in dictResp.keys():
    print(f"{key: <10}:{dictResp[key]: <10}")
