import sys
from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
n, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, sys.stdin.readline().split())
virus = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append([graph[i][j],i,j,0])

q = deque(sorted(virus))
while q:
    ev, ey, ex, et = q.popleft()
    for i in range(4):
        ny = ey + dy[i]
        nx = ex + dx[i]
        if 0<=ny<n and 0<=nx<n and et < s:
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[ey][ex]
                q.append((ev,ny,nx, et+1))

print(graph[x-1][y-1])