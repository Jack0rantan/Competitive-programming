a = list(open('input.txt','r'))
for i in a:
    s = i.replace('\n','')
    ss = s.split(' ')

txt = []
for i in ss:
    txt.append(int(i))
txt = sorted(txt)

res = 0
for j in range(len(txt))[:-1]:
    if j == 0:
        res += (txt[j] + txt[j+1]) / 2
    else:
        res = (res + txt[j+1]) / 2
print(res)
