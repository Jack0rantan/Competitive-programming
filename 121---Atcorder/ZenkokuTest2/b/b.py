input = open('input.txt','r').readline

n = int(input())
d = list(map(int, input().split()))
div = 998244353

dic = {}
for i in d:
    try:
        a = dic[i]
        dic[i] = a + 1
    except:
        dic[i] = 1
ans = 0
if max(d) > 1:
    ans = 1
    for j in range(max(d)+1)[2:]:
        ans *= dic[j-1]**dic[j]

print(ans%div)