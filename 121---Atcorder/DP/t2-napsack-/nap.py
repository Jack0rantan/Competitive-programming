input = open('input.txt','r').readline

# input

n = int(input())
v = [0] * n; w = [0] * n
for i in range(n):
    v[i],w[i] = map(int, input().split())

print(v)
print(w)

# prepare
dp = []
    