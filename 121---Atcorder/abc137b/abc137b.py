import sys

# input file
f = open('testinput_b.txt', 'r')
sys.stdin = f

i = 1
ans = ""
K,X = map(int,input().split())
for x in range(X-K+1,X+K,1):
    ans += str(x)
    if(i != K*2-1):
        ans += " "
    i += 1
print(ans)
