input =  open('input.txt','r').readline

n = int(input())
s = str(input())
if(s == s[0:n//2] + s[0:n//2]):
    print("Yes")
else:
    print("No")
