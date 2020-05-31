a = []
for i in open('input.txt','r'):
    a.append(i.strip())

n = int(a[0]);dict = {}
for i in range(n):
    s = a[i+1].split(' ')
    dict[s[0]] = s[1]

for j in a[n+1:]:
    if dict.get(j,None):
        print(j +'='+dict[j])
    else:
        print('Not found')