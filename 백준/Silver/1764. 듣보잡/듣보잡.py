import sys
n, m = map(int, sys.stdin.readline().split())
dict = {}

cnt = 0
ans = []

for _ in range(n+m):
  s = sys.stdin.readline().strip()
  if s in dict:
    dict[s] += 1
  else:
    dict[s] = 0

for k,v in dict.items():
  if v == 1:
    cnt += 1
    ans.append(k)

print(cnt)

for i in sorted(ans):
  print(i)