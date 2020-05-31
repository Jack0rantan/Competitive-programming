input = open('input.txt','r').readline

n = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
l = make_divisors(n)
if l[len(l)//2]**2 == n:
    print(l[len(l)//2]*2-2)
else:
    print(l[len(l)//2-1]+l[len(l)//2]-2)
