import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sum_arr = [0]
sum_val = 0
for i in arr:
    sum_val += i
    sum_arr.append(sum_val)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_arr[j] - sum_arr[i-1])