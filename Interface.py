import datetime
import os
import subprocess as sp
import threading
import time
import ipScanner


arryAct = []
arryDeAct = []
arryLaAct = []

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def Clear():
    sr = '\033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F \033[F'
    print(sr)

def Title():
    Clear()
    status, result = sp.getstatusoutput("pwd")
    f = open(result + "/Logo/AMA_S.txt", "r")
    next = f.read()
    while next != "":
        print(bcolors.FAIL + next + bcolors.ENDC)
        next = f.read()

def ReadData():
    next = ''
    try:
        status, result = sp.getstatusoutput("pwd")
        f = open(result + "/Ip.txt", "r")
        next = f.readline()
    except:
        next = ''
    for i in range(255):
        ip = ''
        tm = ''
        if next != '':
            ip = next.split(' ')[0]
            ip = ip[0:15]
            tm = next.split(' ')[1]
            tm = tm[0:-2]
            arryAct.append([ip, tm])
            # if arryAct.count([ip, tm]) == 0:
            arryLaAct.append([ip, tm])
            try:
                next = f.readline()
            except:
                ip = ip
        else:
            break

def Print():
    Title()
    ReadData()
    for i in range(9):
        ip = ''
        tm = ''
        try:
            iptm = arryAct.pop(0)
            arryAct.append(iptm)
            ip = iptm[0]
            tm = iptm[1]
        except:
                ip = ip  
        Lip = ''
        Ltm = ''
        for i in range(100):
            try:
                Liptm = arryLaAct.pop(0)
                arryLaAct.append(Liptm)
                if arryAct.count(Liptm) == 0:
                    Lip = Liptm[0]
                    Ltm = Liptm[1]
                    break
            except:
                break
        print('\033[91m    ▐\033[0m' + ip.center(18,' ') + tm.center(18,' ') + '\033[91m▐' + Lip.center(18,' ') + Ltm.center(15,' ') + '▐\033[0m')
    print('\033[91m    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\033[0m')

def Ip_Scan():
    status, result = sp.getstatusoutput('ifconfig | grep "inet " | grep -v 127.0.0.1[2]')
    result = result.split(' ')
    ip = result[len(result) - 1][:result[len(result) - 1].rfind('.')] + '.'
    inputip = input('ip address (difalt "' + ip + '): ')
    if inputip != '':
        ip = inputip
    f = open('s.txt', 'w')
    f.writelines('true')
    while True:
        arryAct.clear()
        a = ipScanner
        a.Serch(ip + '0', ip + '255')
        time.sleep(15)

processThread = threading.Thread(target = Ip_Scan)
processThread.start()

f = open('s.txt', 'w')
f.writelines('fals')

while True:
    status, result = sp.getstatusoutput("pwd")
    f = open(result + "/s.txt", "r")
    next = f.read()
    if next == 'fals':
        continue
    Print()
    time.sleep(5)