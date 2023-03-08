import sys
from collections import deque

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

graph = [[] for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            graph[i].append(j)

def bfs(num):
    chk = [False for _ in range(n)]
    q = deque([num])
    while q:
        e = q.popleft()
        for i in graph[e]:
            if chk[i] == False:
                ans[num][i] = 1
                chk[i] = True
                q.append(i)

for i in range(n):
    if graph[i]:
        bfs(i)

for i in ans:
    print(*i)