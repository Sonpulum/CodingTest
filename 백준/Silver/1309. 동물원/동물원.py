n = int(input())
dp = [0 for _ in range(n)]
for i in range(n):
  if i == 0:
    dp[i] = 3
  elif i == 1:
    dp[i] = 7
  else:
    dp[i] = (dp[i-1] * 2 + dp[i-2])%9901

print(dp[n-1])