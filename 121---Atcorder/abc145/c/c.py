input = open('input.txt','r').readline

def vs(n):
    if n == 2:
        return 1+1
    else:
        return 1+1+ (n-2) * vs(n-1)
def be(n):
    if n ==1:
        return 1
    else:
        return n*be(n-1)

n = int(input())
xarr =[];yarr=[]
la = vs(n); b = be(n)
for i in range(n):
    x,y = map(int, input().split())
    xarr.append(x); yarr.append(y)
c=0
for i in range(n):
    for j in range(n)[i+1:]:
        x1 = (xarr[i] - xarr[j])**2
        y1 = (yarr[i] - yarr[j])**2
        l = (x1+y1)**(1/2)
        c += l * la
print(c/b)