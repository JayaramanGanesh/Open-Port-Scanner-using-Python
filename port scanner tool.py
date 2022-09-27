import pyfiglet
import sys
import socket
from datetime import datetime


banner = pyfiglet.figlet_format("TARGET IP ADDRESS PORT SCANNING")
print(banner)

print("=="*60)
print("the scanner tool use first ur computer and target computer same network")
print(" ")
print("kindly give the target ip address....")
print(" ")
print(" once verified the ip address")
print(" ")
print("scanning start at :" + str(datetime.now()))
print("=="*60)

if len(sys.argv)==2:
    target =socket.gethoustbyname(sys.argv[1])
else:
    print("invvalied arguments")

target_ip = input(str("please give the ip address : "))

try:
    for port in range(1,100000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()
         
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()
except:
       pass