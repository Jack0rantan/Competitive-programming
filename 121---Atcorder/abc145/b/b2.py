f = open('input.txt','r')
input = f.readline

R = lambda:list(map(int,input().split()))
input()
a, b, c = R(), R(), R()
print(sum(b) + sum(c[i - 1] for i, j in zip(a, a[1:]) if j == i + 1))
