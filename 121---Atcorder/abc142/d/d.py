input = open('input.txt','r').readline

n, m = map(int,input().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

# 最大公約数見つける
mx = gcd(n,m)

# 公約数列挙
l =[]
for i in range(1,mx+1):
    if n % i == 0 and m % i == 0:
        l.append(i)
print(l)

# 互いに素の列挙
#
#     この計算ができなかった
#
ans = [1]
for i in l[:1:-1]:
    print(i)
    for j in l[1:]:
        if coprime(i,j) == False:
            break
        else:
            
            if not j in ans:
                ans.append(j)
            else:
                ans.append(i)
print(ans)