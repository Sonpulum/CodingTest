import sys
ans = [i for i in range(1,31)]
for i in range(28):
  a = int(sys.stdin.readline().strip())
  ans.remove(a)
print(ans[0])
print(ans[1])