from heapq import*
que = []
a = []
for x in range(4):
     heappush(que,x)

for x in range(len(que)):
     heappop(que)
     print(que)
     print(que[0])
