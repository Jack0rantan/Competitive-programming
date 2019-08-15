import sys

# input file
f = open('input.txt', 'r')
sys.stdin = f

ans = 0
count = 0
skip = False
N=int(input())
S=[int(x) for x in input().split(" ")]

for i in range(N)[:-1]:
    if skip == True:
        skip = False
        continue
    else:
        ans += 1
        if i+2 > N-1:
            break
        else:
            if S[i+2] == 0:
                count += 2
                skip = True
            else:
                count += 1
                skip = False
            if count >= N-1:
                break
print(ans)
