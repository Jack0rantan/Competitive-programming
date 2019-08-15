import sys

# input file
f = open('testinput_d.txt', 'r')
sys.stdin = f

#import sys
input = sys.stdin.readline

# 逆再生
# 連結成分がくっつくときに加点

N,M = map(int,input().split())
AB = [[int(x) for x in input().split()] for _ in range(M)]

root = list(range(N+1))
comp_size = [1] * (N+1)

def find_root(x):
  y = root[x]
  if x == y:
    return x
  z = find_root(y)
  root[x] = z
  return z

def merge(x,y):
  rx = find_root(x)
  ry = find_root(y)
  if rx == ry:
    return 0
  sx = comp_size[rx]
  sy = comp_size[ry]
  if sx > sy:
    root[ry] = rx
    comp_size[rx] += sy
  else:
    root[rx] = ry
    comp_size[ry] += sx
  return sx * sy

answer = []
x = N*(N-1)//2
for a,b in AB[::-1]:
  answer.append(x)
  x -= merge(a,b)

for a in answer[::-1]:
  print(a)
