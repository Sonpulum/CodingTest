import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
graph_chk = [[0 for _ in range(m)] for _ in range(n)]

def bfs(graph, y, x):
    q = deque()
    q.append([y,x])
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0<=ny<n and 0<=nx<m and graph[ny][nx] != 0:
                if graph_chk[ny][nx] == 0:
                    graph_chk[ny][nx] = graph_chk[ey][ex] + 1
                    q.append([ny,nx])
                else:
                   if graph_chk[ey][ex] + 1 < graph_chk[ny][nx]:
                        graph_chk[ny][nx] = graph_chk[ey][ex] + 1
                        q.append([ny,nx])

px = 0
py = 0

for i in range(n):
    if 2 in graph[i]:
        py = i
        break
px = graph[i].index(2)

bfs(graph,py,px)


for i in range(n):
    for j in range(m):
        if graph_chk[i][j] == 0 and graph[i][j] !=0:
            graph_chk[i][j] = -1
            
graph_chk[py][px] = 0

for i in graph_chk:
    print(*i)