def dfs(arr, idx):
  if len(arr) == m:
    print(*arr)
    return

  for i in range(idx, n):
    arr.append(lst[i])
    dfs(arr,i+1)
    arr.pop()
    
n,m = map(int, input().split())
lst = [i for i in range(1,n+1)]
dfs([],0)