import sys

# input file
f = open('plusminus.txt', 'r')
sys.stdin = f

def plusMinus(arr):
    ans = [0] * 3
    for i in range(n):
        if arr[i] > 0:
            ans[0] += 1
        elif arr[i] < 0:
            ans[1] += 1
        else:
            ans[2] += 1
    for item in [x/n for x in ans]:
        print(item)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
