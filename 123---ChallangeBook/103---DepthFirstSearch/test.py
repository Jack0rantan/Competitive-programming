import sys

f = open('input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int, input().split()))
k = int(input())

def dfs(i, sum):
    if i == n:
        sum == k
        return sum
    if dfs(i+1, sum):
        return True
    if dfs(i+1, sum + a[i]):
        return True
    return False

if dfs(0,0):
    print('Yes')
else:
    print('No')
