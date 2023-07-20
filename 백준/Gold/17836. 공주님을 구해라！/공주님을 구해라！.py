import sys
from collections import deque

n, m, t = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
chk1 = [[0 for _ in range(m)] for _ in range(n)]
chk2 = [[0 for _ in range(m)] for _ in range(n)]

sword = None
t1 = 1e9
t2 = 1e9

q = deque()
q.append([0,0])

while q:
    ey,ex = q.popleft()
    for i in range(4):
        ny = ey + dy[i]
        nx = ex + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] != 1:
                if chk1[ny][nx] == 0:
                    chk1[ny][nx] = chk1[ey][ex] + 1
                    q.append((ny,nx))
                elif chk1[ny][nx] != 0 and chk1[ny][nx] > chk1[ey][ex] + 1:
                    chk1[ny][nx] = chk1[ey][ex]+1
                    q.append((ny,nx))

                if graph[ny][nx] == 2:
                    sword = [ny,nx]

if chk1[n-1][m-1] != 0:
    t1 = chk1[n-1][m-1]

if sword:
    q.append(sword)

    while q:
        ey,ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if chk2[ny][nx] == 0:
                    chk2[ny][nx] = chk2[ey][ex] + 1
                    q.append((ny,nx))
                elif chk2[ny][nx] != 0 and chk2[ny][nx] > chk2[ey][ex] + 1:
                    chk2[ny][nx] = chk2[ey][ex]+1
                    q.append((ny,nx))

    t2 = chk1[sword[0]][sword[1]] + chk2[n-1][m-1]

res = min(t1,t2)

if res > t:
    print("Fail")
else:
    print(res)