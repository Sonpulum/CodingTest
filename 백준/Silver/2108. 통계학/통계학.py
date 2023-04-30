import sys

n = int(sys.stdin.readline().strip())
arr = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])
cnt_dict = {}
max_cnt = 0
cnt = 0

avg = round(sum(arr)/n)
ctr = arr[n//2]
rng = arr[-1] - arr[0]
most = 0

for i in arr:
    if i not in cnt_dict:
        cnt_dict[i] = 1
    else:
        cnt_dict[i] += 1

for v in cnt_dict.values():
    if v > max_cnt:
        max_cnt = v

for k, v in cnt_dict.items():
    if v == max_cnt:
        cnt += 1
        most = k

    if cnt == 2:
        break

print(avg)
print(ctr)
print(most)
print(rng)