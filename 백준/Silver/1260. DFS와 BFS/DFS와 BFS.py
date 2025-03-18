from collections import deque

n, m, v = map(int, input().split())
graph_list = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for i in range(n+1)]

for i in graph_list:
    a,b = i
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()
    
def dfs(graph, start, visit=[]):
    visit.append(start)

    for v in graph[start]:
        if v not in visit:
            dfs(graph, v, visit)

    return visit

def bfs(graph, start, visit=[]):
    queue = deque([start])
    visit.append(start)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visit:
                visit.append(i)
                queue.append(i)

    return visit

print(*dfs(graph, v))
print(*bfs(graph, v))