input = open('input.txt','r').readline

# input 
n = int(input())
a= list(map(int, input().split()))

# DP list & initial value
dp = [0] * (n+4)
dp[0] = 0

# DP
for i in range(n):
    dp[i+1] = max(dp[i], dp[i] + a[i])

# Ans
print(dp[n])