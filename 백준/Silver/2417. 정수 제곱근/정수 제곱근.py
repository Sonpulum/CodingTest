import sys
n = int(sys.stdin.readline().strip())

start = 0
end = 2**63
ans = n

while start <= end:
    mid = (start+end)//2
    if mid**2 >= n:
        ans = min(ans,mid)
        end = mid -1
    else:
        start = mid + 1

print(ans)