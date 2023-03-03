import sys

n, m = map(int, sys.stdin.readline().split())
result = []


def permutation(idx, depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(idx, n+1):
        result.append(i)
        permutation(i, depth+1)
        result.pop()

permutation(1, 0)