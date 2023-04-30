import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(list(set(arr)))
pres_dict = {}
for i in range(len(sorted_arr)):
    if sorted_arr[i] not in pres_dict:
        pres_dict[sorted_arr[i]] = i

for i in range(n):
    if i != n-1:
        print(pres_dict[arr[i]], end=' ')
    else:
        print(pres_dict[arr[i]], end='')