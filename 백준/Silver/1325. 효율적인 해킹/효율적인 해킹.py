import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph=[[]for _ in range(n+1)]
result = []
max_v = 0

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

def dfs(graph,start):
    check = [False]*(n+1)
    cnt = 0
    stack = deque([start])
    check[start] = True
    while stack:
        c = stack.pop()
        for i in graph[c]:
            if check[i] == False:
                stack.append(i)
                check[i] = True
                cnt += 1

    return cnt

for i in range(1,n+1):
    if graph[i]:
        cnt = dfs(graph,i)
        if cnt > max_v:
            max_v = cnt
            result.clear()
            result.append(i)
        elif cnt == max_v:
            result.append(i)

print(*result)