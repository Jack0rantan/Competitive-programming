x = int(input())

def  fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)

def fib(x):
    if x <= 1:
        return x
    return fib(x-1) + fib(x-2)

memo = [0] * (x+1)
def fib_m(n):
    if n <= 1:
        return n
    if memo[n] != 0:
        return memo[n]
    memo[n] = fib_m(n-1) + fib_m(n-2)
    print(memo)
    return memo[n]

print(fib_m(x))
