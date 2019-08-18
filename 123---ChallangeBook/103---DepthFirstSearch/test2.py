import sys

# input part
txt = []
for i in open('input2.txt', 'r'):
    i = i.replace("\n","")
    txt.append(i)

n, m = map(int,txt[0].split())
w =[]
for i in txt[1:]:
    w.append(list(i))

x = [i-1 for i in range(3)]
y = [i-1 for i in range(3)]
def dfs(xx, yy):
    w[xx][yy] = '.'
    for dx in x:
        for dy in y:
            nx = xx+dx
            ny = yy+dy
            if 0 <= nx and nx < n and 0 <= ny and ny < m and w[nx][ny] == 'W':
                return dfs(nx,ny)

res = 0
for i in range(n):
    for j in range(m):
        if w[i][j] == 'W':
            dfs(i,j)
            res += 1

print(res)
