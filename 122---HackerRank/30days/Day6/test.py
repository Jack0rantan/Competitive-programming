import sys

f = open('input.txt','r')
input = f.readline

a = int(input())
s=[]
for _ in range(a):
    s.append(input().split())

def ans(l):
    ev = []
    od = []
    res = []
    for i in range(len(l)):
        if i % 2 == 0:
            ev.append(l[i])
        else:
            od.append(l[i])

    res = ''.join(ev) + ' ' + ''.join(od)
    return res

for u in s:
    print(ans(*u))
