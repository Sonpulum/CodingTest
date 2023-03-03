import sys

def input():
    return sys.stdin.readline().split()

n, m = map(int, input())
arr = sorted(list(map(int, input())))
result = []
chk = [False for _ in range(n)]

def permutation(idx, depth):
    if depth == m:
        print(*result)
        return
    prev = 0
    for i in range(idx, n):
        if not chk[i] and prev != arr[i]:
            chk[i] = True
            result.append(arr[i])
            prev = arr[i]
            permutation(i, depth + 1)
            chk[i] = False
            result.pop()

permutation(0, 0)