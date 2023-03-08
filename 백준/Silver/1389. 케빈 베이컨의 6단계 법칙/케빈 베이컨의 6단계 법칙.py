import sys
from collections import deque

def input():
    return sys.stdin.readline().split()

n, m = map(int, input())
graph = [[] for _ in range(n+1)]
arr = []

for _ in range(m):
    a, b = map(int,input())
    graph[a].append(b)
    graph[b].append(a)

def bfs(num):
    chk = [False for _ in range(n+1)]
    q = deque()
    q.append([num,0])
    chk[num] = True
    res = 0

    while q:
        e,c = q.popleft()
        for i in graph[e]:
            if chk[i] == False:
                chk[i] = True
                q.append([i,c+1])
                res += c+1
    return res

for i in range(1,n+1):
    arr.append(bfs(i))

print(arr.index(min(arr))+1)