f = open('input.txt','r')
input = f.readline

n,k = map(int,input().split())
s = input()

face = sum(s[i-1] == s[i] for i in range(n)[1:])
print(min(face+2*k, n-1))
