n = int(input())
arr = list(map(int, input().split()))
x = int(input())
cnt = 0
total = 0

def coprime(num1,num2):
    while num2 != 0:
        num1 = num1%num2
        num1, num2 = num2, num1
    
    if num1 != 1:
        return False
    else:
        return True
    
for i in range(n):
    if coprime(x,arr[i]):
        cnt += 1
        total += arr[i]

print(total/cnt)