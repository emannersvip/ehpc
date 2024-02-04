#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys

if sys.version_info < (3, 9):
    print('Must have Python version 3.9 or later installed.')
    sys.exit(1)

log_file_path = os.path.abspath('./ehpc_cluster_status.log')

def sanitize_cmds(cmd):
    # List to be used to sanity check inputs
    cluster_commands = ['uname','uptime','free','codename','cpu']
    for ucmd in cluster_commands:
        if cmd in ucmd:
            if 'uname' in cmd:
                return('uname -r') 
            elif 'uptime' in cmd:
                return('uptime')
            elif 'free'in cmd:
                return('free -h')
            elif 'codename' in cmd:
                return('grep VERSION_CODENAME /etc/os-release')
            elif 'cpu' in cmd:
                return('lscpu | grep "CPU(s):"')
            else:
                return('Elmer')
        else:
            print('Unsupported command')

def format_cpu_set_tab(line,n):
    b = ''
    if n == 1:
        a = line.split()
        b = f"{a[0]} {a[1]}"
    elif n == 2:
        a = line.split()
        b = f"{a[0]} {a[1]} {a[2]} {a[3]}"
    else:
        print('format_cpu_set_tab: This should never happen.')
    return b

def format_cpu(result,ip):
    a = result.split('\n')
    if len(a) > 1:
        a[1] = a[1][:0] + "  " + a[1][0:]
        print(f"{ip}: " + format_cpu_set_tab(a[0],1))
        print(f"  : " + format_cpu_set_tab(a[1], 2))
    else:
        print(f"{ip}: " + format_cpu_set_tab(a[0],1))
    return

def ssh_to_host(cmd):
    cluster_ips = ['192.168.1.10','192.168.1.65','192.168.1.66','192.168.1.67','192.168.1.68','192.168.1.84','192.168.1.85','192.168.1.86','192.168.1.175','192.168.68.10','192.168.68.101','192.168.68.102','192.168.68.103','192.168.68.104']

    command = sanitize_cmds(cmd)
    for host_ip in cluster_ips:
        result = subprocess.check_output(["ssh"] + [host_ip, command]).decode("utf-8").strip()

        if cmd == 'cpu':
            format_cpu(result,host_ip)
        else:
            print(f"{host_ip}: {result}")

def main():
    parser = argparse.ArgumentParser(
        prog='easyHPC Cluster Checker',
        description='easyHPC Cluster Status Checker',
        epilog='Text at the bottom of help')
    parser.add_argument('command')
    args = parser.parse_args()

    print('eHPC..!')
    ssh_to_host(args.command)
    sys.exit(0)

if __name__ == '__main__':
    main()
