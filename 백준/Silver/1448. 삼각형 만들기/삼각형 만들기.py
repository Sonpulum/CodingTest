import sys
n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
arr.sort(reverse=True)

ans = -1
for i in range(2,n):
  if arr[i-2] < arr[i-1]+arr[i]:
    ans = arr[i-2]+arr[i-1]+arr[i]
    break

print(ans)