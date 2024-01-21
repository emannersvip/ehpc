# eHPC_Cluster

import shelve
#import sqlite3

from ehpc_login_node import LoginNode
from ehpc_colors import eColors

# TODO:
#   1) Make clear difference between init cluster and create cluster
#       To have an ACTIVE cluster you must have a login node

# DEBUG CODE
debug = 1
if debug:
    dc = '001: '
else:
    dc =''

class Cluster:
    """EHPC class that defines a cluster"""
    def __init__(self,name):
        # A cluster only beconems active when it has a valid login node (role) and scheduler node (role).
        self.status = 0
        self.name   = name
        self.login   = ''
        self.scheduler = ''
        print(f"{dc} New cluster {eColors.CYAN}{name}{eColors.ENDC} initiated:")

    # https://stackoverflow.com/questions/1535327/how-to-print-instances-of-a-class-using-print
    def __repr__(self):
        return "Cluster()"
    def __str__(self):
        cluster_print = f"Cluster name: {self.name}, login: {self.login}, scheduler: {self.scheduler}, status: {self.status}"
        #return 'Member of Cluster'
        return cluster_print

    def get_status(self):
        if self.status:
            print(f"{dc}Cluster {eColors.CYAN}{self.name}{eColors.ENDC} is {eColors.GREEN}ACTIVE{eColors.ENDC}")
        else:
            print(f"{dc}Cluster {self.name} is {eColors.RED}INACTIVE{eColors.ENDC}")
            print(f"{dc}To make cluster active create a new cluster with {eColors.CYAN}`ehpc cluster create <CLUSTER NAME>`{eColors.ENDC}\n")
        return

    def create_cluster(self,name):
        print(f"{dc} Creating cluster {eColors.CYAN}{self.name}{eColors.ENDC}")
        print(f"{dc} A {eColors.CYAN}cluster{eColors.ENDC} needs at least *one* {eColors.CYAN}login{eColors.ENDC} node to become active.")
        print(f"{dc} {eColors.CYAN}Login{eColors.ENDC} node {eColors.CYAN}name{eColors.ENDC}, fqdn <login01.ehpc.org>: ")
        # TODO: Check for fqdn in the future.
        lname = input()
        print(f"{dc} {eColors.CYAN}Login{eColors.ENDC} node {eColors.CYAN}ip{eColors.ENDC} <192.168.100.1>: ")
        lip = input()
        myLoginNode = LoginNode(lname, lip)
        self.status = 1
        return myLoginNode

