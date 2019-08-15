d={}
c=0
for i in open('testinput_c.txt', 'r'):
    i=tuple(sorted(i))
    t=d.get(i,0)
    c+=t
    d[i]=t+1
print(c)
