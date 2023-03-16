import sys
from collections import deque
r, c = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
chk = [[False for _ in range(c)] for _ in range(r)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]

ans = [0,0]

def bfs(y,x,s,w):
    q = deque()
    q.append((y,x))
    s_cnt = s
    w_cnt = w
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey+dy[i]
            nx = ex+dx[i]
            if 0<=ny<r and 0<=nx<c:
                if chk[ny][nx] == False and graph[ny][nx] != '#':
                    chk[ny][nx] = True
                    q.append((ny,nx))
                    if graph[ny][nx] == 'o':
                        s_cnt += 1
                    elif graph[ny][nx] == 'v':
                        w_cnt += 1

    if s_cnt > w_cnt:
        return [s_cnt,0]
    else:
        return [0,w_cnt]



for i in range(r):
    for j in range(c):
        if chk[i][j] == False:
            if graph[i][j] == 'o':
                chk[i][j] = True
                res = bfs(i,j,1,0)
                ans = [ans[i]+res[i] for i in range(2)]
            elif graph[i][j] == 'v':
                chk[i][j] = True
                res = bfs(i,j,0,1)
                ans = [ans[i]+res[i] for i in range(2)]

print(*ans)