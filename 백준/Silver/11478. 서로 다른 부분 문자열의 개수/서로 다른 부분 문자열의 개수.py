import sys
s = sys.stdin.readline().strip()
l = len(s)

dict = {}
cnt = 0

for i in range(l):
  for j in range(i+1,l+1):
    if s[i:j] in dict:
      dict[s[i:j]] += 1
    else:
      dict[s[i:j]] = 1
      cnt += 1

print(cnt)