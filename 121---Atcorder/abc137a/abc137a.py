import sys

# input file
f = open('testinput_a.txt', 'r')
sys.stdin = f

A,B = map(int,input().split())
ans = [A+B, A-B, A*B]
print(sorted(ans, reverse=True)[0])
