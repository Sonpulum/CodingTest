n = int(input())
l = 4
cnt = 0
arr = [1,5,10,50]
result = []
ans = {}

def combi(depth, idx):
  global cnt
  
  if depth == n:
    total = sum(result)
    if total not in ans:
      ans[total] = 1
    else:
      ans[total] += 1
    return
  for i in range(idx,l):
    result.append(arr[i])
    combi(depth+1, i)
    result.pop()

combi(0,0)
print(len(ans))