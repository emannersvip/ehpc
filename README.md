# EasyHPC
A simpler way to manage HPC clusters
=======
0.1a
easyhpc list login
easyhpc list cluster
easyhpc set cluster
easyhpc show diff <node1> <node2>
easyhpc show diff <node1> <node2> --detailed
easyhpc build login login01
easyhpc admini[ster] <node>
easyhpc attach <node> 
--
0.2a
ehpc --create cluster noether
--
0.3a - Persistent 'shelve' storage
./ehpc.py --show cluster beowulf
./ehpc.py --create login login01.beowulf
./ehpc.py --list logins
./ehpc.py --create compute compute01.beowulf
TODO: Create method for create compute that appends to list.
./ehpc.py --create scheduler schedsvr01.beowulf
TODO: Write code to prevent more than one scheduler being added with error message.
./ehpc.py --list scheduler
./ehpc.py --list computes
--
0.4a - 
TODO: Add to Github
./ehpc.py --create compute compute1.hpc.edsonmanners.com
FIX ./ehpc/py -list computes
--
0.5a
Add colors to ./ehpc.py --show cluster beowulf