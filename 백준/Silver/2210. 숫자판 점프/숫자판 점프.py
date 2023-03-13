import sys
from collections import deque

graph = [list(map(str, sys.stdin.readline().split())) for _ in range(5)]
chk = [[False for _ in range(5)] for _ in range(5)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]
ans = set()

def bfs(y,x):
  q = deque()
  q.append((y,x,graph[y][x]))
  while q:
    ey, ex, es = q.popleft()
    for i in range(4):
      ny = ey+dy[i]
      nx = ex+dx[i]
      if 0<=ny<5 and 0<=nx<5:
        ns = es+graph[ny][nx]
        if len(ns) < 6:
          q.append((ny,nx,ns))
        elif len(ns) == 6:
          ans.add(ns)
      

for i in range(5):
  for j in range(5):
    if chk[i][j] == False:
      chk[i][j] = True
      bfs(i,j)

print(len(ans))