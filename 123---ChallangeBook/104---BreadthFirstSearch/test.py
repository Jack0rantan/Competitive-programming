import sys
from heapq import*

# input part
txt = []
for i in open('input.txt', 'r'):
    i = i.replace("\n","")
    txt.append(i)

n, m = map(int,txt[0].split())
maze =[]

for i in txt[1:]:
    maze.append(list(i))

for x in range(n):
    for y in range(m):
        if maze[x][y]=='S':
            sx = x; sy = y
        if maze[x][y]=='G':
            gx = x; gy = y

# moving vector
vx = [-1,0,1,0]
vy = [0,1,0,-1]

INF = 1000 ** 3

def bfs():
    # initialize
    que = []
    d = [[INF for i in range(n)] for j in range(m)]
    heappush(que, [sx,sy])
    d[sx][sy] = 0

    while len(que):
        xy = que[0];heappop(que)

        if xy[0] == gx and xy[1] == gy:
            break
        for i in range(4):
            nx = xy[0]+vx[i]; ny = xy[1]+vy[i]

            if 0 <= nx and nx < n and 0 <= ny and ny < m and maze[nx][ny] != '#' and d[nx][ny] == INF:
                heappush(que,[nx, ny])
                d[nx][ny] = d[xy[0]][xy[1]] + 1

    print(d)
    return d[gx][gy]

res = bfs()
print(res)
