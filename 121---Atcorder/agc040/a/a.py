input = open('input.txt','r').readline

s=str(input())
arr = [0] * (len(s)+1)

for i in range(len(s)):
    if s[i] == '>': continue
    arr[i+1] = arr[i] + 1

for i in range(len(s))[::-1]:
    if s[i] == '<': continue
    
    if arr[i] > arr[i+1]+1:continue
    else: arr[i] = arr[i+1]+1
print(sum(arr))
    
