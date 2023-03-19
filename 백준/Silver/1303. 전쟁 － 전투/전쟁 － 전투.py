import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(m)]
chk = [[False for _ in range(n)] for _ in range(m)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]

cnt_w = 0
cnt_b = 0

def bfs_w(y,x):
  q = deque()
  q.append((y,x))
  cnt = 1
  while q:
    ey, ex = q.popleft()
    for i in range(4):
      ny = ey+dy[i]
      nx = ex+dx[i]
      if 0<=nx<n and 0<=ny<m:
        if graph[ny][nx] == 'W' and chk[ny][nx] == False:
          chk[ny][nx] = True
          q.append((ny,nx))
          cnt += 1
  return cnt**2

def bfs_b(y,x):
  q = deque()
  q.append((y,x))
  cnt = 1
  while q:
    ey, ex = q.popleft()
    for i in range(4):
      ny = ey+dy[i]
      nx = ex+dx[i]
      if 0<=nx<n and 0<=ny<m:
        if graph[ny][nx] == 'B' and chk[ny][nx] == False:
          chk[ny][nx] = True
          q.append((ny,nx))
          cnt += 1
  return cnt**2

for i in range(m):
  for j in range(n):
    if chk[i][j] == False:
      chk[i][j] = True
      if graph[i][j] == 'W':
        cnt_w += bfs_w(i,j)
      else:
        cnt_b += bfs_b(i,j)

print(cnt_w, cnt_b)