import sys
n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
chk = [False for _ in range(n)]
result = []

def permutation(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for i in range(n):
        if chk[i]:
            continue
        chk[i] = True
        result.append(arr[i])
        permutation(depth+1)
        chk[i] = False
        result.pop()

permutation(0)