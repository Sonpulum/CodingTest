import sys

n = int(sys.stdin.readline().strip())
p = [0]+list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
    if i == 1:
        dp[i] = p[i]
    else:
        dp[i] = p[i]
        for j in range(1,i):
            dp[i] = max(dp[i], dp[j]+dp[i-j] )

print(dp[n])