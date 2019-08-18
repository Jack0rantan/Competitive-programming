import sys

f = open('input.txt','r')
sys.stdin = f

N,Q=map(int,input().split())
ans=[0]*N;con=[0]*N;ab=[]
for i in range(N-1):
    a, b = map(int, input().split())
    con[b-1] = a
print(con)

def dfs(Q, X):
    ans[Q-1] += X
    for n in range(N)[Q:]:
        if con[n] == Q:
            dfs(n+1,X)

qx = []
for i in range(Q):
    q, x = map(int, input().split())
    dfs(q, x)

print(*ans)
