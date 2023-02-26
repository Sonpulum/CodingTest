import math
t = int(input())

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i == 0:
            return False
    return True

for _ in range(t):
    n = int(input())
    while not is_prime(n):
        n+=1
    print(n)