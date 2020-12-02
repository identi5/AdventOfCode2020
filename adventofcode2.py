numbers = []
character = []
password = []
lowlim = []
uplim = []
legalpasswords = 0
i = 0
with open('aocip2.txt','r') as ip:
    for aline in ip:
        numbers.append(aline.split()[0])
        character.append(aline.split()[1][0])
        password.append(aline.split()[2])
for allnos in numbers:
    lowlim.append(int(allnos.split('-')[0]))
    uplim.append(int(allnos.split('-')[1]))
for i in range(len(numbers)):
    if password[i].count(character[i]) >= lowlim[i] and password[i].count(character[i]) <= uplim[i]:
        legalpasswords = legalpasswords + 1
print(legalpasswords)

