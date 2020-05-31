input = open('input.txt','r').readline


from math import*;g=gcd(*map(int,input().split()));d={};i=2
while i*i<=g:
    if g%i:i+=1
    else:g//=i;d[i]=d.get(i,0)+1
if g>1:d[g]=d.get(g,0)+1
print(len(d)+1)
