import sys
input = sys.stdin.readline

n , q = map(int, input().split())

tree = {}
for i in range(n-1):
    a, b = map(int, input().split())
    if a in tree:
        tree[a].append(b)
    else:
        tree[a] = [b]

op = [0] * (n+1)
for i in range(q):
    p, x = map(int, input().split())
    op[p] += x

for root, reaf in tree.items():
    for i in reaf:
        op[i] += op[root]

print(*op[1:])
