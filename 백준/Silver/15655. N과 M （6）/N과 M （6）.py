import sys
n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
chk = [False for _ in range(n)]
result = []

def permutation(idx, depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for i in range(idx, n):
        if chk[i]:
            continue
        chk[i] = True
        result.append(arr[i])
        permutation(i, depth+1)
        chk[i] = False
        result.pop()

permutation(0,0)