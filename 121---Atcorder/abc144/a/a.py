input = open('input.txt','r').readline
ams = 0
a,b = map(int, input().split())
if (a >10 or b > 10):
    ans = -1
else:
    ans = a*b
print(ans)