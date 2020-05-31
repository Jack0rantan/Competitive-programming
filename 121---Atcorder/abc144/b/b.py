input =  open('input.txt','r').readline

n = int(input())
ans = 0
flg = False

for i in range(10)[1:]:
  ans = n/i
  r = n%i
  if(ans<10 and r ==0):
    flg = True
    break
if(flg):
    print("Yes")
else:
    print("No")
