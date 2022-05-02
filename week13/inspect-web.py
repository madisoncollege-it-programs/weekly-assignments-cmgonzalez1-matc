#!/usr/bin/env python3

import requests,bs4

res = requests.get('http://notpurple.com')
res.raise_for_status()

myHTML = bs4.BeautifulSoup(res.text,features="html.parser")
print(myHTML.title.text)

myLinks = myHTML.select('a')
for link in myLinks:
    print(f"=========="*5)
    print(f"{link}")
    input("Press Enter to Continue")

print("Done!")

