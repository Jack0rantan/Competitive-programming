import sys

# input file
f = open('testinput.txt', 'r')
sys.stdin = f

def miniMaxSum(arr):
    t=0
    ar = sorted(arr)
    for i in ar:
        t += i
    print(*[t-ar[4],t-ar[0]])


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
