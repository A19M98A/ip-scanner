import datetime
import os
import subprocess as sp
import threading
import time

def IpCheck(ip):
    try:
        status, result = sp.getstatusoutput("ping -c1 " + str(ip))
        if status == 0:
            arry = result.split(' ')
            for i in arry:
                if i.split('=')[0] == 'time':
                    f = open('Ip.txt', 'a')
                    f.writelines(ip + ' ' + i.split('=')[1] + '\n')
                    
    except Exception:
        return

def Serch(IpStart, IpEnd):
    
    os.system('rm Ip.txt')

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
        for b in range(IpS2 if a == IpS1 else 0, IpE2 + 1 if a == IpE1 else 256):
            for c in range(IpS3 if b == IpS2 else 0, IpE3 + 1 if b == IpE2 else 256):
                for d in range(IpS4 if c == IpS3 else 0, IpE4 + 1 if c == IpE3 else 256):
                    ip2 = str(a) + "." + str(b) + "." + str(c) + "." + str(d)
                    while True:
                        if len(threading.enumerate()) > 200:
                            time.sleep(5)
                        else:
                            break
                    try:
                        processThread = threading.Thread(target = IpCheck, args = (ip2,))
                        tr.append(processThread)
                        processThread.start()
                    except Exception:
                        ip2 = ip2
