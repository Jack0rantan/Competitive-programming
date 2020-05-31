input = open('input.txt','r').readline

A,B = map(int,input().split())
kuti = 1
k = 0
for i in range(100):
    if kuti>=B:
        print(k)
        break
    elif B == 1:
        print(0)
    else:
        kuti += A-1
        k += 1
