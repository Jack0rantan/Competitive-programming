input = open('input.txt','r').readline

N = int(input())
H = list(map(int,input().split()))
k = 0
ans = []
for i in range(N-1):
    if H[i]>H[i+1] or H[i] == H[i+1]:
        k = k+1
    else:
        ans.append(k)
        k = 0
ans.append(k)
print(max(ans))
