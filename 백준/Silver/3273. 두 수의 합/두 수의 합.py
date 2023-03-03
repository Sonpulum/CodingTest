n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
s = 0
e = n-1
cnt = 0

while e != s:
    if arr[e]+arr[s] > x:
        e -= 1
    elif arr[e]+arr[s] < x:
        s += 1
    else:
        cnt += 1
        s += 1

print(cnt)