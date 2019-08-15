import sys

# input file
f = open('input.txt', 'r')
sys.stdin = f

l = int(input())
n = int(input())
x = input().split()

a_min = 0
a_max = 0

for i in x:
    a_min = max(a_min, min(int(i), l-int(i)))
    a_max = max(a_max, max(int(i), l-int(i)))
print(a_min)
print(a_max)
