import datetime
import os
import subprocess as sp
import threading
import time
import signal
import sys

ip = '192.168.1.'
start = 0
end = 255

def signal_handler(signal, frame):
        ansowr = input('cheng to normal DHCP (y/n) => ')
        if ansowr == 'y':
                os.system('networksetup -setdhcp Wi-Fi')
        sys.exit(0)
        
def Chenge():
        for i in range(start, end + 1):
                print(ip + str(i))

                os.system('networksetup -setmanualwithdhcprouter Wi-Fi ' + ip + str(i))

                time.sleep(7)

                status, result = sp.getstatusoutput("ping -c1 google.com")
                if status == 0:
                        break

signal.signal(signal.SIGINT, signal_handler)

status, result = sp.getstatusoutput('ifconfig | grep "inet " | grep -v 127.0.0.1[2]')
result = result.split(' ')
ip = result[len(result) - 1][:result[len(result) - 1].rfind('.')] + '.'
inputip = input('ip address (difalt "' + ip + '): ')
if inputip != '':
        ip = inputip

while True:
        inputstart = input('start (difalt 0): ')
        if inputstart != '':
                start = int(inputstart)
        inputend = input('end (difalt 255) : ')
        if inputend != '':
                end = int(inputend)
        Chenge()
        sys.stdout.flush()
        ansowr = input('\acontinu (y/n) => ')
        if ansowr == 'n':
                ansowr = input('cheng to normal DHCP (y/n) => ')
                if ansowr == 'y':
                        os.system('networksetup -setdhcp Wi-Fi')
                        break
                break




# def ChengeMacAddress():
#         status, result = sp.getstatusoutput("openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//'")
#         os.system('sudo ifconfig en0 ether ' + result)