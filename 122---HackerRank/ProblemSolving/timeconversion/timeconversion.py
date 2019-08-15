import sys

# input file
f = open('testinput.txt', 'r')
sys.stdin = f

def timeConversion(s):
    #
    # Write your code here.
    #
    time = s.strip('APM')
    h = int(time[0:2])
    if s[-2] == "A" and h == 12:
        print("00"+time[2:])
    elif s[-2] == "A" or h == 12:
        print(time)
    h += 12
    print(str(h)+time[2:])

if __name__ == '__main__':
    s = input()

    timeConversion(s)
