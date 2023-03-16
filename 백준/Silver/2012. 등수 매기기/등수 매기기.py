import sys
n = int(sys.stdin.readline().strip())
arr = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])
res = [abs(arr[i]-(i+1)) for i in range(n)]
print(sum(res))