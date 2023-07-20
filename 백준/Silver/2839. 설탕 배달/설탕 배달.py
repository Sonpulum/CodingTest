import sys

n = int(sys.stdin.readline().strip())
dp = [-1 for _ in range(n+1)]

for i in range(3, n+1):
    if i == 3:
        dp[i] = 1
    elif i == 5:
        dp[i] = 1
    else:
        if dp[i-3] != -1 and dp[i-5] != -1:
            dp[i] = min(dp[i-3],dp[i-5])+1
        elif dp[i-3] != -1 and dp[i-5] == -1:
            dp[i] = dp[i-3] + 1
        elif dp[i-5] != -1 and dp[i-3] == -1:
            dp[i] = dp[i-5] + 1
        else:
            dp[i] = -1

print(dp[n])