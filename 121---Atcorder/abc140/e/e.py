input = open('input.txt','r').readline

n = int(input())
*p, = map(int,input().split())


#--------------------------------------
#   for文を２回繰り返した時点で TLE になる
#   P(n**2)は通らない、ということ。
#--------------------------------------
ans = 0
for i in range(n-1):
    for j in range(n)[i+1:]:
        ans += sorted(p[i:j+1])[-2]

print(ans)