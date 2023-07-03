import sys

k, n = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline().strip()) for _ in range(k)]

start = 1
end = max(lines)

while start <= end:
    mid = (start + end) // 2
    res = 0
    for i in lines:
        res += (i // mid)
    if res >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)