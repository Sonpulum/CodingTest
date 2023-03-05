import sys

arr = list(map(str, sys.stdin.readline().strip()))
stack = []
ans = 0

for i in range(len(arr)):
    if arr[i] == "(":
        stack.append("(")
    else:
        if arr[i-1] == "(":
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1

print(ans)