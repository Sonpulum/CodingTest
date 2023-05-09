import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())

total_arr = [0 for _ in range(n+1)]
total = 0
for i in range(1,n+1):
  total += a[i-1]
  total_arr[i] = total

for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())
  print(total_arr[j]-total_arr[i-1])