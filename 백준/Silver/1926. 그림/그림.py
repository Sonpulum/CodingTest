import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chk = [[False for _ in range(m)] for _ in range(n)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]
cnt = 0
max_area = 0

def bfs(y,x):
    q = deque()
    q.append((y,x))
    area = 1

    while q:
        ey,ex = q.popleft()
        for i in range(4):
            ny = ey+dy[i]
            nx = ex+dx[i]

            if 0<=ny<n and 0<=nx<m:
                if chk[ny][nx] == False and graph[ny][nx] == 1:
                    chk[ny][nx] = True
                    q.append((ny,nx))
                    area += 1
    return area

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            max_area = max(max_area, bfs(i,j))
            cnt += 1

print(cnt)
print(max_area)