import sys

# input file
f = open('testinput.txt', 'r')
sys.stdin = f

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    dict = {}
    for i in ar:
        t = dict.get(i,0)
        dict[i] = t + 1
    print(dict[max(ar)])

if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    birthdayCakeCandles(ar)
