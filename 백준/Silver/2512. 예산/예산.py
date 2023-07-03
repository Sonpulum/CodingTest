import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    cur = 0
    for i in arr:
        if i > mid:
            cur += mid
        else:
            cur += i
    if cur <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)