#

import shelve
sh = shelve.open('ehpc.shelf')

#from ehpc.ehpc_cluster import Cluster
#from ehpc.ehpc_login_node import LoginNode
#from ehpc.ehpc_scheduler_node import SchedulerNode
from ehpc_cluster import Cluster
from ehpc_login_node import LoginNode
from ehpc_scheduler_node import SchedulerNode

debug = 1

mycluster = 0
mylogin = 0
mycompute = 0
myscheduler = 0

def cluster_add():
    if cluster_status != True:
        ehpc_cluster = Cluster('Noether')
        try:
            sh['cluster'] = ehpc_cluster
            print(f"Added new Cluster {ehpc_cluster.name}")
        except:
            print('Cant add new Cluster')
    return
def login_add():
    if cluster_status() == True and login_status() == False:
        ehpc_login = LoginNode('pi-robot-2', '192.168.68.102')
        try:
            sh['login'] = ehpc_login
            print(f"Added new Login Node: {ehpc_login.name}")
        except:
            print('Cant add new Login Node')
    else:
        print('Else??')
    return
def scheduler_add():
    if cluster_status() == True and scheduler_status() == False:
        ehpc_scheduler = SchedulerNode('pi-robot-3', '192.168.68.103')
        try:
            sh['scheduler'] = ehpc_scheduler
            print(f"Added Scheduler Node: {ehpc_scheduler.name}")
        except:
            print('Cant add Scheduler Node')
    else:
        print('Else??')

def cluster_info():
    if debug: print('CLUSTER INFO')
    if login_status() == False: login_cnt = 0
    else: login_cnt = 1

    try:
        if sh['cluster']:
            print('============================')
            print(f"{sh['cluster'].name}")
            print('============================')
            print(f"Login Nodes:   {login_cnt}")
            print(f"Compute Nodes: 0")
            print(f"Schedulers:    0\n")
            print('Hint: Please create a login node using: `login add <bob.login>`')
    except KeyError as e:
        print('No cluster defined. Create a cluster using: `cluster add <bob>`')
    return
def cluster_status():
    try:
        if sh['cluster']: return 1
    except KeyError as e:
        print('No cluster defined. Create a cluster using: `cluster add <bob>`')
    return 0

def login_info():
    try:
        if sh['login']:
            print('============================')
            print(f"{sh['login'].name}")
            print('============================')
            print(f"Login Node:   {sh['login'].name}")
            print('Hint: Please create a scheduler using: `scheduler add <bob.scheduler>`')
    except KeyError as e:
        print('No login node defined. Create a login node using: `login add <bob.login>`')
    return
def login_status():
    try:
        if sh['login']: return 1
    except KeyError as e:
        print('No login node defined. Create a login node using: `login add <bob.login>`')
    return 0

def scheduler_info():
    try:
        if sh['scheduler']:
            print('============================')
            print(f"{sh['scheduler'].name}")
            print('============================')
            print(f"Scheduler:   {sh['scheduler'].name}")
            print('Hint: Please add compute nodes using: `compute add <bob.compute>`')
    except KeyError as e:
        print('No scheduler defined. Create a scheduler using: `scheduler add <bob.scheduler>`')
    return
def scheduler_status():
    try:
        if sh['scheduler']: return 1
    except KeyError as e:
        print('No scheduler defined. Create a scheduler using: `scheduler add <bob.scheduler>`')
    return 0

cluster   = 0
login     = 0
scheduler = 0

while 1:
    try:
        text = input('eHPC > ')
        cli_cmd = text.split()
        for parameter in cli_cmd:
            if parameter == 'quit' or parameter == 'exit':
                exit()
            elif parameter == 'add':
                if cluster: cluster_add() ; cluster = 0
                elif login: login_add() ; login = 0
                elif scheduler: scheduler_add() ; scheduler = 0
                else: print('Unhandled ADD')
            elif parameter == 'cluster':
                cluster = 1
                if debug: print(f"Cluster: cli_cmd: {cli_cmd} parameter: {parameter}")
                next
            elif parameter == 'debug':
                print(f"{cli_cmd} : {parameter}")
            elif parameter == 'info':
                if debug: print(f"INFO: {cli_cmd}")
                if cluster: cluster_info() ; cluster = 0
                elif login: login_info() ; login = 0
                elif scheduler: scheduler_info() ; scheduler = 0
                else: print('Unhandled INFO')
            elif parameter == 'list':
                pass
            elif parameter == 'login':
                login = 1
                next
            elif parameter == 'scheduler':
                scheduler = 1
                next
            elif parameter == 'show':
                pass
            elif parameter == 'status':
                if cluster: cluster_status() ; cluster = 0 ; print('Cluster PRESENT\n')
                elif login: login_status() ; login = 0 ; print('Login Node PRESENT\n')
                elif scheduler: scheduler_status() ; scheduler = 0 ; print('Scheduler Node PRESENT\n')
                else: print('Unhandled STATUS')
            else:
                print(f"unhandled {parameter}")
    except KeyboardInterrupt:
        print('Goodbye...')
        exit()

sh.sync() ; sh.close()