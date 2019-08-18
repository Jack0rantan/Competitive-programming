import sys

f = open('input.txt','r')
input = f.readline

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = [0] * n
    for i in range(n):
        res[n-i-1] = arr[i]
    print(*res)
