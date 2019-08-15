import sys

# input file
f = open('input.txt', 'r')
sys.stdin = f

n = int(input())
a = input().split()
ans = 0

for i in range(n):
    for j in range(n)[i+1:]:
        for k in range(n)[j+1:]:
            len = int(a[i])+int(a[j])+int(a[k])
            ma = max(int(a[k]), max(int(a[i]),int(a[j])))
            rest = len - ma
            if ma < rest:
                ans = max(ans, len)

print(ans)
