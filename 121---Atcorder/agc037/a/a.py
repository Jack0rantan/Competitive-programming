import sys

f = open('input.txt','r')
sys.stdin = f

s = input()
skip = False
ans = [s[0]]
n = 0
for i in range(len(s))[1:]:
    if skip == True:
        skip = False
        continue
    elif ans[n] == s[i] and i+1 < len(s):
        ans.append(s[i]+s[i+1])
        skip = True
        n += 1
    else:
        ans.append(s[i])
        n += 1
res = len(ans)
if ans[-1] == ans[-2]:
    res -= 1
print(res)
