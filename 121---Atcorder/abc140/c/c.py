f = open('input.txt','r')
input = f.readline

n = int(input())
b = list(map(int, input().split()))

ans = b[0]
for i in range(n-1)[:-1]:
    ans += min(b[i],b[i+1])
    
print(ans+b[-1])