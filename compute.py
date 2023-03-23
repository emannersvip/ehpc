#!/usr/bin/python3

import re
import subprocess

# Prettify 'free -h'
def mem_prettify(mem):
    return mem.split()[1]
# Prettify 'df -h'
def disk_prettify(disk):
    return disk.split()[0] + ' ' + disk.split()[3]
# Get HostName
result = subprocess.run(['hostname', '-f'], stdout=subprocess.PIPE)
print("\n" + result.stdout.decode('utf-8').rstrip())
# Get CPU Info
result = subprocess.run(['lscpu'], stdout=subprocess.PIPE, text=True)
list1 = result.stdout.splitlines()

for line in list1:
     if re.search('Model name', line):
        cpu_gen = line.split('name:')[1].strip()
     if re.search('Core\(s\)', line):
        cpu_cor = line.split('socket:')[1].strip()
     if re.search('Socket', line):
        cpu_soc = line.split('Socket(s):')[1].strip()

# Get Memory info
result = subprocess.run(['free', '-h'], stdout=subprocess.PIPE, text=True)
list1 = result.stdout.splitlines()

for line in list1:
     if re.search('Mem:', line):
        mem = mem_prettify(line)

# Get Disk info
result = subprocess.run(['lsblk'], stdout=subprocess.PIPE, text=True)
list1 = result.stdout.splitlines()

for line in list1:
     if re.search('disk', line):
        disk = disk_prettify(line)

print(' - CPU:  ' + cpu_gen + ', ' + cpu_cor + ' Core, ' + cpu_soc + ' Socket')
print(' - RAM:  ' + mem)
print(' - Disk: ' + disk)
