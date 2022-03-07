#! /usr/bin/env python3
#[Lab-Python] Dictionaries
#Christian Gonzalez

#Creating a mapping of server's FQDN to server's IP's
FQDN = {
    'server1.testlab.com': '192.168.1.10',
    'server2.testlab.com': '192.168.1.11',
    'server3.testlab.com': '192.168.1.12',
    'server4.testlab.com': '192.168.1.13',
    'server5.testlab.com': '192.168.1.14',
    'server6.testlab.com': '192.168.1.15'
}


#Listing all of the FQDN's in my dictionary
for fqdn, ip in list(FQDN.items()):
    print(f"{fqdn}")

print('-' * 40)
#Listing all of the IP Addresses in my dictionary
for fqdn, ip in list(FQDN.items()):
    print(f"{ip}")

print('-' * 40)
#List all of the full records (key/value pairs)
for fqdn, ip in list(FQDN.items()):
    print(f"{fqdn}: {ip}")
print("-" * 40)

#Add a few more names
FQDN['server7.testlab.com'] = '192.168.1.16'
FQDN['server8.testlab.com'] = '192.168.1.17'
#Test if server2 is contained in your dict.
print(f"server2.testlab.com")
print("-" * 40)
#Test if server10 is contained in your dict.
server = FQDN.get('server10.testlab.com')
print(f"{server}")
