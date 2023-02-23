import sys
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

cnt_B = 0
cnt_R = 0

for i in range(n):
  if s[i] == 'R':
    if i == 0  :
      cnt_R += 1
    else:
      if s[i-1] == 'B':
        cnt_R += 1

for i in range(n):
  if s[i] == 'B':
    if i == 0  :
      cnt_B += 1
    else:
      if s[i-1] == 'R':
        cnt_B += 1
          
print(min(cnt_B, cnt_R)+1)