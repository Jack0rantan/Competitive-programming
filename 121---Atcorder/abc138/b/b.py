a = list(open('input.txt','r'))
for i in a:
    s = i.replace('\n','')
    txt = s.split(' ')

res = 0
for i in txt:
    res += 1/int(i)

print(1/res)
