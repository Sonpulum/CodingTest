import sys
n, m = map(int, sys.stdin.readline().split())
val = []
cnt = 0

for _ in range(n):
  p, l = map(int,sys.stdin.readline().split())
  arr = sorted(list(map(int, sys.stdin.readline().split())))

  if l > p:
    val.append(1)

  else:
    val.append(arr[p-l])

val.sort()
total = 0

for i in val:
  total += i
  if total<=m:
    cnt += 1
  else:
    break

print(cnt)
  