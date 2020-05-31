input = open('input.txt','r').readline

a = int(input())
#------------------------------------
#   ↓　読み込みにfor文を使うな。
#------------------------------------
t = [int(s) for s in input().split()]

s = [0] * (len(t)-1)

for j in range(len(t)-1):
    count = 0
    if t[j] > t[j+1]:
        s[j] = 1

an = []
ans = ''.join([str(_) for _ in s]).split('0')
for _ in ans:
    an.append(len(_))

print(max(an))
