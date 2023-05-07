import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
chk_dist = [0 for _ in range(n)]

max_dist = 0
max_cnt = 0
max_num = 0

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

q = deque()
q.append((0))
chk_dist[0] = 1
while q:
    ex = q.popleft()
    for i in graph[ex]:
        if chk_dist[i] == 0:
            chk_dist[i] = chk_dist[ex] + 1
            q.append(i)
        elif chk_dist[i] > chk_dist[ex] + 1:
            chk_dist[i] = chk_dist[ex] + 1
            q.append(i)

for i in range(n):
    if chk_dist[i] > max_dist:
        max_dist = chk_dist[i]
        max_cnt = 1
        max_num = i
    
    elif chk_dist[i] == max_dist:
        max_cnt += 1

print(max_num+1, max_dist-1, max_cnt)