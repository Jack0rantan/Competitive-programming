input = open('input.txt','r').readline

import heapq

n = int(input())
a = list(map(int, input().split()))
dic = {}; ans = []
for i in range(n+1)[1:]:
    dic.setdefault(a[i-1],[]).append(i)
heapq.heapify(a)
for i in range(n):
    res = heapq.heappop(a)
    ans.append(dic[res][0])
print(*ans)