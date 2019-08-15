import sys

# input file
f = open('testinput.txt', 'r')
sys.stdin = f

def if_else(n):
    if n%2 != 0 or (6<=n and n<=20):
        print("Weird")
    else:
        print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())
    if_else(n)
