import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
ans = ''
cnt = 0

for i in range(m):
    max_v = 0
    dict = {'A':0,'C':0,'G':0,'T':0}
    for j in range(n):
        e = arr[j][i]
        dict[e] += 1
        if max_v < dict[e]:
            max_v = dict[e]

    for k,v in dict.items():
        if v == max_v:
            ans += k
            break

for i in range(n):
    for j in range(m):
        if ans[j] != arr[i][j]:
            cnt += 1

print(ans)
print(cnt)