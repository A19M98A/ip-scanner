import datetime
import os
import subprocess as sp
import threading
import time

# @staticmethod
def IpCheck(ip):
    # print(ip)
    try:
        status, result = sp.getstatusoutput("ping -c1 " + str(ip))
        if status == 0:
            # print(ip + ' OK')
            arry = result.split(' ')
            for i in arry:
                # print("---> " + i + " <--- : " + datetime.datetime.now())
                if i.split('=')[0] == 'time':
                    # print('\033[94m' + ip + '\033[0m')
                    # print(ip + '\t time = ' + i.split('=')[1] + ' ms')
                    f = open('Ip.txt', 'a')
                    f.writelines(ip + ' ' + i.split('=')[1] + '\n')
                    # print(ip + ' ' + i.split('=')[1])
                    
    except Exception:
        return

# Main Projeckt
############################################################################
# Heder()
# clear()
# @staticmethod
def Serch(IpStart, IpEnd):
    try:
        os.system('rm Ip.txt')
    except:
        ab = 1
    # IpStart = '192.168.43.0' #input("   Enter the ip address (EX:192.168.1.1):\t")
    # IpEnd = '192.168.43.255' #input("   Enter The End Ip (EX:192.168.1.255):\t\t")
    # Title()

    # print('\n\n----------------------------\n')
    # print('   < Ip > \t  < ping time >\n')

    Ip_S = IpStart.split(".")
    Ip_E = IpEnd.split(".")
    IpS1 = int(Ip_S[0])
    IpS2 = int(Ip_S[1])
    IpS3 = int(Ip_S[2])
    IpS4 = int(Ip_S[3])
    IpE1 = int(Ip_E[0])
    IpE2 = int(Ip_E[1])
    IpE3 = int(Ip_E[2])
    IpE4 = int(Ip_E[3])

    tr = []

    for a in range(IpS1, IpE1 + 1):
        # print('a -> ' + str(a))
        for b in range(IpS2 if a == IpS1 else 0, IpE2 + 1 if a == IpE1 else 256):
            # print('b -> ' + str(b))
            for c in range(IpS3 if b == IpS2 else 0, IpE3 + 1 if b == IpE2 else 256):
                # print('c -> ' + str(c))
                for d in range(IpS4 if c == IpS3 else 0, IpE4 + 1 if c == IpE3 else 256):
                    ip2 = str(a) + "." + str(b) + "." + str(c) + "." + str(d)
                    while True:
                        if len(threading.enumerate()) > 200:
                            time.sleep(5)
                            # print('wait --> ' + ip2)
                        else:
                            break
                    # print('d -> ' + str(d))
                    try:
                        # print(ip2)
                        processThread = threading.Thread(target = IpCheck, args = (ip2,))
                        tr.append(processThread)
                        processThread.start()
                    except Exception:
                        ip2 = ip2

# Serch('192.168.1.0', '192.168.1.255')