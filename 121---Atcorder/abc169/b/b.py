input = open('input.txt','r').readline

# なぜかエラー


import numpy as np

n = int(input())
A = list(map(int, input().split()))
AA = int(np.prod(A))

if AA > 10**18:
    print(-1)
else:
    print(AA)