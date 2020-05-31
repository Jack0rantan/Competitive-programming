input = open('input.txt','r').readline

import heapq

n = int(input())
l = list(map(int,input().split()))
l = list(map(lambda x: x * (-1), l))
heapq.heapify(l)

ans = 0
while len(l) >= 3:
    mx = heapq.heappop(l) * (-1)
    for i in range(len(l)-1):
        for j in range(len(l))[i+1:]:
            if mx < (l[i] + l[j]) * (-1):
                ans += 1

print(ans)