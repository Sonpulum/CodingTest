import sys
from collections import deque

def input():
    return sys.stdin.readline().split()

m, n, k = map(int,input())
arr = [list(map(int, input())) for _ in range(k)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]

graph = [[0 for _ in range(n)] for _ in range(m)]
chk = [[False for _ in range(n)] for _ in range(m)]
ans=[]
for i in arr:
    s_x, s_y, e_x, e_y = i
    for y in range(s_y,e_y):
        for x in range(s_x,e_x):
            graph[y][x] = 1

def bfs(y, x):
    q = deque()
    q.append([y,x])
    cnt = 1
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey+dy[i]
            nx = ex+dx[i]
            if 0<=ny<m and 0<=nx<n:
                if graph[ny][nx] == 0 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append([ny,nx])
                    cnt += 1

    return cnt

cnt = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and chk[i][j] == False:
            cnt += 1
            chk[i][j] = True
            ans.append(bfs(i,j))

print(cnt)
print(*sorted(ans))