import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
chk = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
dx = [-1,0,0,0,0,1]
dy = [0,-1,1,0,0,0]
dz = [0,0,0,-1,1,0]
start = deque()
isAble = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                start.append((i,j,k,0))

def bfs(q):
    while q:
        ez, ey, ex, ec = q.popleft()
        for i in range(6):
            nz = ez+dz[i]
            ny = ey+dy[i]
            nx = ex+dx[i]

            if 0<=nz<h and 0<=ny<n and 0<=nx<m:
                if graph[nz][ny][nx] == 0 and chk[nz][ny][nx] == False:
                    graph[nz][ny][nx] = 1
                    chk[nz][ny][nx] = True
                    q.append((nz,ny,nx,ec+1))

    return ec

if start:
    res = bfs(start)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                isAble = False
                break
        if isAble == False:
            break
    if isAble == False:
        break

if isAble == False:
    print(-1)
else:
    print(res)