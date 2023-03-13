import sys
s = sys.stdin.readline().strip()
ucpc_str = ''
for i in s:
    if i == 'U' and len(ucpc_str) == 0:
        ucpc_str += i
    elif i == 'C' and (len(ucpc_str) == 1 or len(ucpc_str) == 3):
        ucpc_str += i
    elif i == 'P' and len(ucpc_str) == 2:
        ucpc_str += i

if ucpc_str == "UCPC":
    print("I love UCPC")
else:
    print("I hate UCPC")