input = open('input.txt','r').readline


# -----------------------------
#   d3.py を参考に
#   d.py　をheapqを使って実装
# -----------------------------
import heapq

n, m = map(int,input().split())
s = list(map(int, input().split()))
s = list(map(lambda x: x * (-1), s))
heapq.heapify(s)

for i in range(m):
    mx = heapq.heappop(s) * (-1)
    mx = mx//2
    heapq.heappush(s, mx*(-1))
    
print(sum(s)*(-1))