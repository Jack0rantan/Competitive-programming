input = open('input.txt','r').readline

n = int(input())
s = list(input())
ans = 1
be = s[0]
for st in s[1:]:
    if be != st:
        ans += 1
        be = st
print(ans)