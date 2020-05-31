f = open('input.txt','r')
input = f.readline

s = str(input())
ans = 'Yes'
for i in list(s)[0::2]:
    if i == 'L':
        ans = 'No'
for i in list(s)[1::2]:
    if i == 'R':
        ans = 'No'
print(ans)
    