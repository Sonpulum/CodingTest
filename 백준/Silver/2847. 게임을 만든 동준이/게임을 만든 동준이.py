n = int(input())
q = []

ans = 0

for _ in range(n):
    q.append(int(input()))

for i in reversed(range(1,n)):
    if q[i] <= q[i-1]:
        v = q[i-1]-q[i]+1
        q[i-1] -= v
        ans += v

print(ans)