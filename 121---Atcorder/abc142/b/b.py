input =  open('input.txt','r').readline

_,k = map(int, input().split())
h = list(map(int, list(input().split())))
print(sum(map(lambda x : x>=k, h)))
