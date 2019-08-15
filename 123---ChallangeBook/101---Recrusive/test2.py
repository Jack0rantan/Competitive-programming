from heapq import*
que = []
a = []
for x in range(4):
     heappush(que,x)
print(que)
for x in range(len(que)):
     heappop(que)
     print(sorted(que))
