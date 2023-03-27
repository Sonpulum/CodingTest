import sys
from collections import deque

chk = [-1 for _ in range(100001)]

n, k = map(int, sys.stdin.readline().split())

if n == k:
  print(0)
else:
  q = deque()
  q.append((n,0))
  chk[n] = 0
  res = []
  while q:
    e, t = q.popleft()
    if e == k:
      res.append(t)
    for i in range(3):
      if i == 0:
        if 0<=e-1<=100000:
          if chk[e-1] == -1:
            chk[e-1] = t+1
            q.append((e-1,t+1))
          else:
            if chk[e-1] > t+1:
              chk[e-1] = t+1
              q.append((e-1,t+1))

      elif i == 1:
        if 0<=e+1<=100000:
          if chk[e+1] == -1:
            chk[e+1] = t+1
            q.append((e+1,t+1))
          else:
            if chk[e+1] > t+1:
              chk[e+1] = t+1
              q.append((e+1,t+1))
      else:
        if 0<=e*2<=100000:
          if chk[e*2] == -1:
            chk[e*2] = t
            q.append((e*2,t))
          else:
            if chk[e*2] > t:
              chk[e*2] = t
              q.append((e*2,t))
  print(min(res))