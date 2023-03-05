import sys

n = int(sys.stdin.readline().strip())
f = int(sys.stdin.readline().strip())

arr = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ex = 0
ey = -1
v = n**2
fx = 0
fy = 0

while n >= 1:
    for i in range(4):
        if i == 0:
            for j in range(n):
                ex = ex + dx[i]
                ey = ey + dy[i]
                arr[ey][ex] = v
                if v == f:
                    fx = ex
                    fy = ey
                v -= 1
        elif i == 1:
            for j in range(n-1):
                ex = ex + dx[i]
                ey = ey + dy[i]
                arr[ey][ex] = v
                if v == f:
                    fx = ex
                    fy = ey
                v -= 1
        elif i == 2:
            for j in range(n-1):
                ex = ex + dx[i]
                ey = ey + dy[i]
                arr[ey][ex] = v
                if v == f:
                    fx = ex
                    fy = ey
                v -= 1
        else:
            for j in range(n-2):
                ex = ex + dx[i]
                ey = ey + dy[i]
                arr[ey][ex] = v
                if v == f:
                    fx = ex
                    fy = ey
                v -= 1
    n = n-2

for i in arr:
    print(*i)
print(fy+1,fx+1)