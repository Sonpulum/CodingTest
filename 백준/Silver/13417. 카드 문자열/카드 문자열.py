from collections import deque
import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
  n = int(sys.stdin.readline().strip())
  s = list(map(str, sys.stdin.readline().split()))
  ans = deque()
  ans.append(s[0])
  p = s[0]
  for i in range(1,n):
    if s[i] > p:
      ans.append(s[i])
    else:
      ans.appendleft(s[i])
      p = s[i]

  print(*ans,sep='')