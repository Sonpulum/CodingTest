import sys
from collections import deque
dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

n = int(sys.stdin.readline().strip())
r1,c1,r2,c2 = map(int, sys.stdin.readline().split())

q = deque()
q.append((r1,c1))
chk_m = [[0 for _ in range(n)] for _ in range(n)]
chk_m[r1][c1] = 1
while q:
    er, ec = q.popleft()
    for i in range(6):
        nr = er + dr[i]
        nc = ec + dc[i]
        if 0<=nr<n and 0<=nc<n:
            if chk_m[nr][nc] == 0:
                chk_m[nr][nc] = chk_m[er][ec] + 1
                q.append((nr,nc))
            elif chk_m[nr][nc] > chk_m[er][ec] + 1:
                chk_m[nr][nc] = chk_m[er][ec] + 1
                q.append((nr,nc))

print(chk_m[r2][c2] - 1)