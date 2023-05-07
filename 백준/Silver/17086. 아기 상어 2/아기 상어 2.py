import sys
from collections import deque
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,1,0,1,-1,-1,1,0]
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chk_dist = [[0 for _ in range(m)] for _ in range(n)]
max_dist = 0

def bfs(y,x):
    q = deque()
    q.append((y,x))
    while q:
        ey, ex = q.popleft()
        for i in range(8):
            ny = ey+dy[i]
            nx = ex+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if graph[ny][nx] == 0:
                    if chk_dist[ny][nx] == 0:
                        chk_dist[ny][nx] = chk_dist[ey][ex] + 1
                        q.append((ny,nx))
                    elif chk_dist[ny][nx] > chk_dist[ey][ex] + 1:
                        chk_dist[ny][nx] = chk_dist[ey][ex] + 1
                        q.append((ny,nx))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i,j)

for i in chk_dist:
    max_dist = max(max_dist,max(i))

print(max_dist)
