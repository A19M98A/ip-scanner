arryAct = []
arryLaAct = []

# arryAct.append(['192.168.43.255', '0.063'])
# arryAct.append(['192.168.43.1', '0.063'])
# arryLaAct.append(['192.168.43.255', '0.063'])
# arryLaAct.append(['192.168.43.1', '0.063'])
arryLaAct.append(['192.168.43.2', '0.063'])

print(arryAct.count(1))

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
    while 1:
        try:
            Liptm = arryLaAct.pop(0)
            arryLaAct.append(Liptm)
            Lip = Liptm[0]
            Ltm = Liptm[1]
            if arryAct.count(Liptm) == 0:
                break
        except:
            break

    print('\033[91m    ▐\033[0m' + ip.center(18,' ') + tm.center(18,' ') + '\033[91m▐' + Lip.center(18,' ') + Ltm.center(18,' ') + '▐\033[0m')