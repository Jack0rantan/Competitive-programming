f = open('input.txt','r')
input = f.readline

a=[]
n, k, q = map(int, input().split())
for _ in range(q):
    ss = input().split()
    a.append(int(ss[0]))
ans = [k-q] * n
for i in a:
    ans[i-1] = ans[i-1] + 1

for i in ans:
    if i > 0:
        print('Yes')
    else:
        print('No')