from colorama import Fore, Back, Style

import os
import sqlite3
import subprocess

# https://www.w3schools.com/python/python_file_remove.asp
# https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3
if os.path.exists('arp.db'):
    os.remove('arp.db')
connection = sqlite3.connect('arp.db')

# https://www.geeksforgeeks.org/print-colors-python-terminal/
print(Fore.CYAN + 'Welcome to Network Scanner!')
#print(Fore.CYAN + 'Some CYAN Text')
print('Some CYAN Text')
print(Back.GREEN + 'With GREY background')
print(Style.DIM + "and in DIM text")
print(Style.RESET_ALL)
print('All back to normal now')

cursor = connection.cursor()
cursor.execute('CREATE TABLE arp (hostname TEXT, ip TEXT, mac TEXT, nic TEXT)')
cursor.execute('INSERT INTO arp VALUES ("bob", "10.0.0.0", "aa:bb:cc:dd:ee:ff", "eth0")')
rows = cursor.execute('SELECT hostname, ip, mac, nic FROM arp').fetchall()

process = subprocess.run(['/usr/sbin/arp','-a'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#print(process.stdout)
#print(process.stderr)

# n_host, n_ip, n_mac, n_int
for i in process.stdout.splitlines():
    line = i.split()
    # Process hostname
    if line[0]=='?':
        n_host = 'tbd'
    else:
        n_host = line[0]
    # Process IP
    # https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
    # Remove first & last characters from string.
    n_ip = line[1][1:-1]
    # Check for incomplete MAC
    if line[3]=='<incomplete>':
        n_mac=line[3][1:-1]+'-MAC'
    else:
        n_mac=line[3]
    # Handle NIC
    if len(line)==6:
        n_int=line[5]
    else:
        n_int=line[6]

    # Finally print/insert the entry
    print(Fore.CYAN + n_host + ' ' + Fore.MAGENTA + n_ip + ' ' + Fore.GREEN + n_mac + ' ' + Fore.BLUE + n_int, end = '')
    print(Style.RESET_ALL)





