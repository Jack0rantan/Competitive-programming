#Write your code here
class Calculator:
    def power(self,x,y):
        if x < 0 or y < 0:
            raise ValueError('n and p should be non-negative')
        else:
            return x ** y 

myCalculator=Calculator()

f = open('input.txt','r')
input = f.readline

T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   