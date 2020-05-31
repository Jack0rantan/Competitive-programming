input = open('input.txt','r').readline

n = int(input())
arl=[];arr=[]
for i in range(n):
    l,r = map(int, input().split())
    arl.append(l)
    arr.append(r)

pl1 = arr[0] - arl[0] +1 ; pl2 = arr[1] - arl[1]+1

print(pl1 + pl2)
