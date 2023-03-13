import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
graph = [['.' for _ in range(m)] for _ in range(n)]
chk = [[False for _ in range(m)] for _ in range(n)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]
max_size = 0

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    graph[r-1][c-1] = '#'

def bfs(y,x):
    q = deque()
    q.append((y,x))
    size = 1

    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey+dy[i]
            nx = ex+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if graph[ny][nx] == '#' and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append((ny,nx))
                    size += 1

    return size

for i in range(n):
    for j in range(m):
        if graph[i][j] == '#' and chk[i][j] == False:
            chk[i][j] = True
            max_size = max(max_size,bfs(i,j))

print(max_size)