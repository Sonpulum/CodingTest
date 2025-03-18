import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(st_x, st_y):
    visit_graph = [[False for _ in range(m)] for _ in range(n)]

    que = deque()
    que.append((st_x,st_y))

    while que:
        cur_x, cur_y = que.popleft()
        visit_graph[cur_y][cur_x] = True
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < m and 0 <= next_y < n:
                if graph[next_y][next_x] != 0 and visit_graph[next_y][next_x] == False:
                    graph[next_y][next_x] = graph[cur_y][cur_x] + 1
                    que.append((next_x, next_y))
                    visit_graph[next_y][next_x] = True
bfs(0,0)
print(graph[n-1][m-1])
