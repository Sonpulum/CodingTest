import sys

x = list(map(str, sys.stdin.readline().strip()))
l = len(x)
chk = [False for _ in range(l)]
able = False
ans = int(1e9)

result = []

def backtr():
    global able
    global ans

    if len(result) == l:
        if int(''.join(result)) > int(''.join(x)):
            ans = min(ans,int(''.join(result)))
            able = True
            return
    for i in range(l):
        if chk[i]:
            continue
        chk[i] = True
        result.append(x[i])
        backtr()
        chk[i] = False
        result.pop()

backtr()

if not able:
    ans = 0

print(ans)