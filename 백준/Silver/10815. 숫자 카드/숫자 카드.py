import sys

n = int(sys.stdin.readline().strip())
a = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline().strip())
b = list(map(int, sys.stdin.readline().split()))
ans = [[0] for _ in range(m)]

def binarySearch(find, start, end):
    if start>end:
        return 0
    
    mid = (start+end)//2
    if a[mid] == find:
        return 1
    elif a[mid] < find:
        return binarySearch(find, mid+1, end)
    else:
        return binarySearch(find, start, mid-1)

for i in range(m):
    ans[i] = binarySearch(b[i], 0, n-1)

print(*ans)