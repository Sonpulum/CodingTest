import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

dict = {}
cnt = 0

for i in a+b:
  if i in dict:
    dict[i] += 1
  else:
    dict[i] = 1

for v in dict.values():
  if v == 1:
    cnt += 1

print(cnt)