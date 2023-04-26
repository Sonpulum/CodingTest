import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
a_r = a[::-1]

dp1 = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]
result = 0

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp1[i] = max(dp1[i], dp1[j] +  1)
        if a_r[i] > a_r[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)


dp2 = dp2[::-1]
for i in range(n):
    ans = dp1[i] + dp2[i]
    result = max(result,ans)

print(result-1)