import sys
n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key = lambda x : (x[0],x[1]))
ans = 0

for i in range(n):
  if i == 0:
    ans = arr[0][0] + arr[0][1]
  else:
    if ans >= arr[i][0]:
      ans += arr[i][1]
    else:
      ans = arr[i][0] + arr[i][1]

print(ans)