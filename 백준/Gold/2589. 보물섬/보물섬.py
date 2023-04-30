from collections import deque
import sys

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

h, w = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(h)]
ans = 0

def bfs(y,x):
    t = 0
    chk = [[0 for _ in range(w)] for _ in range(h)]
    q = deque()
    q.append((y,x))
    chk[y][x] = 1
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]

            if 0<=ny<h and 0<=nx<w:
                if graph[ny][nx] == 'L':
                    if chk[ny][nx] == 0:
                        chk[ny][nx] = chk[ey][ex] + 1
                        q.append((ny,nx))
                    elif chk[ny][nx] > chk[ey][ex] + 1:
                        chk[ny][nx] = chk[ey][ex] + 1
                        q.append((ny,nx))

    for i in chk:
        t = max(t, max(i))

    return t

for i in range(h):
    for j in range(w):
        if graph[i][j] == 'L':
            ans = max(ans, bfs(i,j))

print(ans-1)