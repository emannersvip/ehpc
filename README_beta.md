# EasyHPC
A simpler way to manage HPC clusters
=======
0.1rc
easyhpc cluster status
easyhpc cluster add bob
easyhpc login status
easyhpc login add bob.login
...
easyhpc show diff <node1> <node2>
easyhpc show diff <node1> <node2> --detailed
easyhpc build login login01
easyhpc admini[ster] <node>
easyhpc attach <node> 

STATUS:
-- The 'status' verb is a BOOL that returns the existence of at least one object of the intended class
-- To get a 'report' of the intended class use 'cluster info or login info'