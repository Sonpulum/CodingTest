import sys

def input():
    return sys.stdin.readline()

n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []

def permutation(depth, idx):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(idx, n):
        result.append(arr[i])
        permutation(depth+1, i)
        result.pop()

permutation(0,0)