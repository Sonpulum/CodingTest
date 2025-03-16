from collections import deque
n,m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

chk = [[False]*m for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    chk[x][y] = True
    while queue:
        ex,ey = queue.popleft()

        for k in range(4):
            nx = ex+dx[k]
            ny = ey+dy[k]

            if 0<=nx<m and 0<=ny<n:
                if chk[ny][nx] == False and graph[ny][nx] == 1:
                    chk[ny][nx] = True
                    graph[ny][nx] += graph[ey][ex]
                    queue.append((nx,ny))


bfs(0,0)
print(graph[n-1][m-1])