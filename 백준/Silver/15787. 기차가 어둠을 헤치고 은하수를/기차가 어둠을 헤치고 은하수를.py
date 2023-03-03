from collections import deque

n, m = map(int, input().split())
train = [deque([0 for _ in range(20)]) for _ in range(n)]
ans = []
cnt = 0

for _ in range(m):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        train[cmd[1]-1][cmd[2]-1] = 1
    
    elif cmd[0] == 2:
        train[cmd[1]-1][cmd[2]-1] = 0
    
    elif cmd[0] == 3:
        train[cmd[1]-1].appendleft(0)
        train[cmd[1]-1].pop()

    else:
        train[cmd[1]-1].append(0)
        train[cmd[1]-1].popleft()

for i in train:
    if i not in ans:
        ans.append(i)
        cnt += 1

print(cnt)