import sys

# input file
f = open('testinput_c.txt', 'r')
sys.stdin = f

N = int(input())
S = []
for _ in range(N):
    S.append("".join(sorted(list(input()))))

ans = 0
memo = [x for x in range(N)]
for x in range(N-1):
    for y in range(1,N):
        if S[x] == S[y] and memo[x] != memo[y]:
            memo[y] = memo[x]

for x in range(N):
    con = memo.count(x)
    if con != 0:
        ans += con*(con-1)//2

print(ans)
