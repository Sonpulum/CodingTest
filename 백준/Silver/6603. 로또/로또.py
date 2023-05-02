import sys

while True:
    a = list(map(int, sys.stdin.readline().split()))
    k = a[0]
    s = a[1:]

    if not s:
        break

    result = []
    chk = [False for _ in range(k)]

    def combi(Depth, idx):
        if Depth == 6:
            print(*result)
            return
        else:
            for i in range(idx, k):
                if chk[i]:
                    continue
                chk[i] = True
                result.append(s[i])
                combi(Depth+1, i)
                chk[i] = False
                result.pop()

    combi(0,0)
    print()