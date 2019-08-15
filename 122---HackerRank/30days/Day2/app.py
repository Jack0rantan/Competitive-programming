str=[]
# when you submit, you should change contents of open-fucntion to open(0)
txt = [x for x in open('input.txt','r')]
for x in txt:
    str.append(x.replace("\n", ""))

cost = float(str[0])
tip = float(str[1])
tax = float(str[2])

ans = cost*(1+(tip+tax)/100)
if ans-int(ans) < 0.5:
    print(int(ans))
else:
    print(int(ans)+1)
