#!/usr/bin/env python3

import requests
#Getting the page
print("Grabbing page from https://notpurple.com")
response = requests.get("https://notpurple.com")

#Copying it to a file called my_web_file.html
print("Copying text and pasting to my_web_file.html")
with open("my_web_file.html", "w") as hFile:
    hFile.write(response.text)
print("Done")
