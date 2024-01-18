# eHPC_Login

import socket
import subprocess

from .ehpc_colors import eColors

# DEBUG CODE
debug = 1
if debug:
    dc = '002: '
else:
    dc =''

class LoginNode:
    """EHPC class that defines Login Nodes"""
    def __init__(self, name, ip):
        self.name    = name
        self.ip      = ip
        self.idm     = 'local'  # Choose AD,LDAP,sssd, etc.
        self.storage = 'local'
        # I expect this to be set at the cluster level in the future.
        # For now it'll be split from the fqdn
        self.domain  = 'ehpc.org' 

        ename = self.name.split('.')
        ename.pop(0)
        self.domain = '.'.join(ename)

    def __repr__(self):
        return "Login()"
    def __str__(self):
        login_print = f"LoginNode name: {self.name}, ip: {self.ip}, idm: {self.idm}, storage: {self.storage}, domain: {self.domain}"
        return login_print
    def get_status(self):
        if self.name and self.ip:
            print(f"{dc}Login Node, {eColors.CYAN}{self.name}{eColors.ENDC}, is {eColors.GREEN}ACTIVE{eColors.ENDC}")

    def getName(self):
        return self.name
    def checkDNS(self):
        try:
            #addrInfo = socket.getaddrinfo(self.name, 22)
            addrInfo = socket.gethostbyname(self.name)
            print(f"  IP:   {addrInfo}")
            return 1
        except socket.gaierror as e:
            print(f"  --{dc}Failed DNS forward check: {e}")
            return 0
        finally:
            return
    def checkPing(self):
        #command = ['ping', '-c', '1', '-w2', self.ip]
        command = ['ping', '-c1', '-w1', self.ip]
        if subprocess.run(args=command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
            print(f"  Ping: TRUE")
            return 1
        else:
            #print(f"  --{dc}Failed Ping check.")
            print(f"  Ping: FALSE")
            return 0
    def checkSSH(self):
        #command = 'uptime'
        command = ['ssh', self.ip, 'uptime']
        if subprocess.run(args=command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
        #print(subprocess.check_call(['ssh', self.ip, 'command']))
            print(f"  SSH:  TRUE")
            return 1
        else:
            print(f"  SSH:  FALSE")
            return 0
    def checkScheduler(self):
        command = 'sinfo'
        print(subprocess.check_call(['ssh', self.ip, 'command']))

    def validateNode(self):
        retval=False
        #TODO:
        # Check DNS (For simple forward DNS lookups, it's better to use socket.getaddrinfo() or socket.gethostbyname().)
        self.checkDNS()
        # Ping IP
        # Login with SSH (First check for saved SSH Key for eHPC)
        # https://stackoverflow.com/questions/1939107/python-libraries-for-ssh-handling
        if self.checkPing():
            if self.checkSSH():
                # Optional (doesn't cause a failed test) Run sinfo and other scheduler equivalent
                # need to write a global check to see if a scheduler exists in a cluster before this can be run
                #self.checkScheduler()
                retval = True
        else:
            print(f"  --Will try SSH check after ping is successful or disabled")
        return retval
