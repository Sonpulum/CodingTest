s1 = input()
k = input()
s2 = ''

for i in s1:
    if not i.isdecimal():
        s2 += i

if k in s2:
    print(1)
else:
    print(0)