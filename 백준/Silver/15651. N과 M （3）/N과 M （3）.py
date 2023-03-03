import sys

n, m = map(int, sys.stdin.readline().split())
result = []


def permutation(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        result.append(i)
        permutation(depth+1)
        result.pop()

permutation(0)