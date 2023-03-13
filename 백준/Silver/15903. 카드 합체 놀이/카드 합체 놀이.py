import sys
n, m = map(int, sys.stdin.readline().split())
cards = sorted(list(map(int, sys.stdin.readline().split())))

for _ in range(m):
    res = cards[0] + cards[1]
    cards[0] = res
    cards[1] = res
    cards.sort()

print(sum(cards))