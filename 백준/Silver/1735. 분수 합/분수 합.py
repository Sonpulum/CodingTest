a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

a3 = a1 * b2 + a2 * b1
b3 = b1 * b2


def lcm(n, m):
  while n > 0:
    m = m % n
    n, m = m, n

  return m

c = lcm(a3,b3)
print(a3//c, b3//c)
