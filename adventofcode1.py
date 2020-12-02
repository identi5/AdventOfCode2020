iplist = []
sortlist = []
with open('aocip1.txt','r') as Input1:
    for aline in Input1:
        iplist.append(int(aline))
sortlist = sorted(iplist)
for i in range(len(sortlist)):
    for j in range(i, len(sortlist)):
        for k in range(j, len(sortlist)):
            if sortlist[i] + sortlist[j] + sortlist[k] == 2020:
                print(sortlist[i] * sortlist[j] * sortlist[k])
                break