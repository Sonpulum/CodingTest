import sys

def input():
    return sys.stdin.readline().split()

n, m = map(int, input())
arr = sorted(list(map(int, input())))
result = []

def permutation(depth):
    if depth == m:
        print(*result)
        return
    prev = 0
    for i in range(n):
        if prev != arr[i]:
            result.append(arr[i])
            prev = arr[i]
            permutation(depth + 1)
            result.pop()

permutation(0)