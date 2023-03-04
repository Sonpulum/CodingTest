import sys
n = int(sys.stdin.readline().strip())
mine_graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
open_graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]

dx=[-1, -1, -1, 0, 0, 1, 1, 1]
dy=[1, 0, -1, 1, -1, 1, 0, -1]

def open_mine():
  for i in range(n):
    for j in range(n):
      if mine_graph[i][j] == '*':
        open_graph[i][j] = '*'
        
for i in range(n):
  for j in range(n):
    if open_graph[i][j] == 'x':
      if mine_graph[i][j] == '*':
        open_mine()

      else:
        mine_cnt = 0
        for k in range(8):
          nx = j+dx[k]
          ny = i+dy[k]
          if 0<=nx<n and 0<=ny<n:
            if mine_graph[ny][nx] =='*':
              mine_cnt += 1

        open_graph[i][j] = mine_cnt

for i in open_graph:
  print(''.join(map(str,i)))