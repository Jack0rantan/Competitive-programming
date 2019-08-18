import sys

f = open('input.txt','r')
sys.stdin = f


N = int(input())
v = list(map(int, input().split()))

v.sort(reverse = True)

for i in range(N-1):
    a = v.pop()
    b = v.pop()
    v.append((a+b)/2)
    v.sort(reverse = True)

print(v[0])
