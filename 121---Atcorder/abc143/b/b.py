input =  open('input.txt','r').readline

n = int(input())
d = list(map(int, input().split()))
ans = 0

for i in range(n)[:-1]:
    for j in range(n)[i+1:]:
        ans += d[i]*d[j]

print(ans)