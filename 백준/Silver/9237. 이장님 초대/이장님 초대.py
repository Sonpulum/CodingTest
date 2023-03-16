import sys
n = int(sys.stdin.readline().strip())
arr = sorted(list(map(int, sys.stdin.readline().split())))
arr = [arr[i]-i for i in range(n)]

print(max(arr)+n+1)