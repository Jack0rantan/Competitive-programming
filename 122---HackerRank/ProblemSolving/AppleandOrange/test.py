str = []
for x in open('input.txt', 'r'):
    str.append(x.replace('\n','').split(' '))

s = int(str[0][0])
t = int(str[0][1])
a = int(str[1][0])
b = int(str[1][1])
app = int(str[2][0])
ora = int(str[2][1])
dis_app = str[3]
dis_ora = str[4]

def cF(ll):
    count = 0
    for x in ll:
        if s <= int(x) and int(x) <= t:
            count += 1
    return count

def toAbsApp(x):
    return int(x)+a
def toAbsOra(x):
    return int(x)+b

dis_app = list(map(toAbsApp, dis_app))
dis_ora = list(map(toAbsOra, dis_ora))

print(cF(dis_app))
print(cF(dis_ora))
