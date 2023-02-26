import sys
n = int(sys.stdin.readline().strip())
arr = sorted(list(map(int, sys.stdin.readline().split())))
arr2 = [i/2 for i in arr[:-1]]
print(sum(arr2)+arr[-1])