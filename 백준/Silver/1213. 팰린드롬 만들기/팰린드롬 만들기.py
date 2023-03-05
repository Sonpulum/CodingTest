import sys

s = sorted(list(map(str, sys.stdin.readline().strip())))
d = {}
ans = ''
ans2 = ''
cent = ''

cnt_odd = 0

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

p = 0

for k,v in d.items():
    if v%2 != 0:
        cnt_odd += 1
        cent = k
        v -= 1
        ans = ans + k*(v//2)
    else:
        ans = ans + k*(v//2)

    if cnt_odd >= 2:
        break

if cnt_odd>=2:
    print("I'm Sorry Hansoo")

else:
    for i in reversed(ans):
        ans2 = ans2 + i
    print(ans+cent+ans2)