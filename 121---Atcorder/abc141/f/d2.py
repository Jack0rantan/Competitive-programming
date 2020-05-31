f = open('input.txt','r')
input = f.readline

# n,k=map(int,input().split());s=input();print(min(sum(s[i-1]==s[i]for i in range(1,n))+k*2,n-1))

n,k=map(int,input().split())
s=input()

#---------------------------------------------------------
# print(sum(s[i-1]==s[i]for i in range(1,n)))
#---------------------------------------------------------
# sum([True,True]) は 2　となる。

print(min(sum(s[i-1]==s[i]for i in range(1,n))+k*2,n-1))
