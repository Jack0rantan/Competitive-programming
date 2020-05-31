input = open('input.txt','r').readline

A, B = map(int, input().split())
ans = 0;count=1
while B > count:
    if B==1:
        print(0)
        break
    else:
        ans += 1
        count += A-1
print(ans)