import sys

n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))

result = []


def permutation(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for i in range(n):
        result.append(arr[i])
        permutation(depth+1)
        result.pop()

permutation(0)