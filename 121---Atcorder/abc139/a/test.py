f = open('input.txt','r')
input = f.readline

count = 0
S = list(input())
T = list(input())
for i in range(len(T)):
    if S[i] == T[i]:
        count += 1
print(count)