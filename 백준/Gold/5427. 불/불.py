import sys
from collections import deque
t = int(sys.stdin.readline().strip())
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
res = []
for _ in range(t):
  w, h = map(int, sys.stdin.readline().split())
  graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(h)]
  chk = [[0 for _ in range(w)] for _ in range(h)]
  chk_f = [[False for _ in range(w)] for _ in range(h)]
  
  fire = []
  s = []
  ans = int(1e9)
  flag = False
  
  for i in range(h):
    for j in range(w):
      if graph[i][j] == '*':
        fire.append([i,j,0])
        chk_f[i][j] = True
      elif graph[i][j] == '@':
        s.append([i,j,1])
        chk[i][j] = 1
        if i-1 == h or j-1 == w:
          ans = 1
          flag = True
          break
          
  if flag:
    res.append(ans)
    continue
        
  q = deque(fire+s)
  
  while q:
    ey, ex, ef = q.popleft()
    for i in range(4):
      ny = ey + dy[i]
      nx = ex + dx[i]
      if 0<=ny<h and 0<=nx<w:
        if ef == 0:
          if graph[ny][nx] == '.':
            if chk_f[ny][nx] == False:
              graph[ny][nx] = '*'
              q.append([ny,nx,0])
        elif ef == 1:
          if graph[ny][nx] == '.':
            if chk[ny][nx] == 0:
              chk[ny][nx] = chk[ey][ex] + 1
              q.append([ny,nx,1])
            elif chk[ny][nx] > chk[ey][ex] + 1:
              chk[ny][nx] = chk[ey][ex] + 1
              q.append([ny,nx,1])

  for i in range(h):
    if 0 < chk[i][0]:
      ans = min(ans,chk[i][0])
    if 0 < chk[i][w-1]:
      ans = min(ans,chk[i][w-1])

  for j in range(w):
    if 0 < chk[0][j]:
      ans = min(ans, chk[0][j])
    if 0 < chk[h-1][j]:
      ans = min(ans, chk[h-1][j])

  if ans < int(1e9):
    res.append(ans)
  else:
    res.append("IMPOSSIBLE")

for i in res:
  print(i)