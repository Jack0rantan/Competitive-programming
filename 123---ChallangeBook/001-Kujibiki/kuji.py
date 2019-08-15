#n, m, k = [x for x in open("testinput.txt", "r")]
import sys

# input file
f = open('questions.txt', 'r')
sys.stdin = f

n = int(input())
m = int(input())
k = input().split()
ans = False

for a in k:
    for b in k:
        for c in k:
            for d in k:
                if int(a)+int(b)+int(c)+int(d) == m:
                    ans = True
print(ans)
