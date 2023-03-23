#!/usr/bin/python3

# https://docs.python.org/3/library/argparse.html#action
import argparse
# https://www.tutorialspoint.com/python_data_persistence/python_data_persistence_quick_guide.htm
import shelve

def ehpc_create(create):
    if create == None:
        return
    elif create[0] == 'cluster':
        db['clusters']=create[1]
        print('Cluster "' + create[1] + '" created.')
    elif create[0] == 'login':
        db['logins']=create[1]
        print('Login Node "' + create[1] + '" created.')
    elif create[0] == 'compute':        # Computes can have multiple nodes
        try:
            print(db['computes'])
        except KeyError:
            print('No existing computes so there\'s nothing to print.')
        finally:
            append_computes(create[1])
            print('Compute Node "' + create[1] + '" created.')
    elif create[0] == 'scheduler':
        db['schedulers']=create[1]
        print('Scheduler "' + create[1] + '" created.')
    else:
        print('Unknown output create')
        print(create)
    return
def ehpc_list(list):
    if list == 'cluster':
        if db['clusters']:
            print(db['clusters'])
        else:
            print('Empty cluster: Create a new cluster?')
    elif list == 'logins':
        if db['logins']:
            print(db['logins'])
        else:
            print('No Login Nodes Defined: Add one?')
    elif list == 'computes':
        try:
          if db['computes']:
            print(db['computes'])
        except KeyError:
            print('No Compute Nodes Defined: Create one?')
    elif list == 'scheduler':
        if db['schedulers']:
            print(db['schedulers'])
        else:
            print('No schedulers Defined: Add one?')
    elif list == None:
        return
    else:
        print('Unknown output list')
    return
# Set a Vaule
def ehpc_set(set):
    if set != None:
        print(set)
# Show a specific value
def ehpc_show(show):
    if show != None:
        print('Cluster name: ' + show[0])
        print('---- Login Node(s):     ' + getLoginNodes())
        print('---- Scheduler Node(s): ' + getSchedulerNodes())
        print('---- Compute Node(s):   ', end='')
        print(getComputeNodes())

def getLoginNodes():
    foo = db.get('logins')
    if foo == None:
        print('**** No Login nodes exist: Create one with `./ehpc.py --create login login01.beowulf`')
        return '**** NONE'
    else:
        return db['logins']

def getSchedulerNodes():
    foo = db.get('schedulers')
    if foo == None:
        print('**** No Schedulers exist: Create one with `./ehpc.py --create scheduler schedsvr01.beowulf`')
        return '\n**** NONE'
    else:
        return db['schedulers']
def getComputeNodes():
    foo = db.get('computes')
    if foo == None:
        print('\n**** No Compute Nodes exist: Create one with `./ehpc.py --create compute compute01.beowulf`')
        return '**** NONE'
    else:
        return db['computes']

def append_computes(tail):
    # Add error handling for adding the first compute
    tmp_list = []
    try:
        #if type(tail) is str:           # This happens for the first compute node
        if type(db['computes']) is str:           # This happens for the first compute node
            tmp_list.append(tail)
            tmp_list.append(db['computes'])
        else:
            tmp_list = list(db['computes'])
            tmp_list.append(tail) 
    except KeyError:
        print('Adding first compute node..')
        db['computes'] = tail
        return
    db['computes'] = tmp_list
    #print(db['computes'])
    return

# Global Variables
# TODO: Change list to data structure that does now allow dupes
ehpc_clusters = []

# Persistent Storage
db = shelve.open('cluster.db')

parser = argparse.ArgumentParser(
    prog='ehpc',
    description='Fully and comprehensively manage your HPC cluster',
    epilog='2023 Koballion')

parser.add_argument('--create', dest='create', help='Create action', nargs=2, required=False)
parser.add_argument('--list', dest='list', help='List action', nargs='?')
parser.add_argument('--set', dest='set', help='Set action', nargs='?')
parser.add_argument('--show', dest='show', help='Show action', nargs=2, required=False)
#parser.add_argument('--list', dest='accumulate', action='store_const',
#                    const=sum, default=max, required=False,
#                    help='sum the integers (defatul: find max)')
parser.add_argument('-V', '--version', action='version', version='%(prog)s 0.5a')
parser.add_argument('-v', '--verbose', action='store_true')

args = parser.parse_args()

#print(args.create)
#print(args.list)
#print(args.show)
#print(args.set)

ehpc_create(args.create)
ehpc_list(args.list)
ehpc_show(args.show)
ehpc_set(args.set)

# Close the program cleanly.
db.close()