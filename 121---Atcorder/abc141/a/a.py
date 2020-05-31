import sys

f = open('input.txt','r')
sys.stdin = f

s = input()
dict = {1:'Sunny', 2:'Cloudy', 3:'Rainy'}
for i in range(1,4):
    if s == dict[i]:
        if i < 3:
            print(dict[i+1])
            break
        else:
            print(dict[1])
        