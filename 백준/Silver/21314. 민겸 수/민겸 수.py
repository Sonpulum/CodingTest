import sys
s = sys.stdin.readline().strip()
arr = []
max_v = ''
min_v = ''
p = 0

for i in range(len(s)):
    if s[i] == 'K':
        arr.append(s[p:i+1])
        p = i+1
    
    else:
        if i == len(s)-1:
            arr.append(s[p:i+1])

for i in arr:
    if 'M' in i and 'K' in i:
        m_cnt = i.count('M')
        max_v += '5'+'0'*m_cnt
        min_v += str(10**(m_cnt-1))+'5'
    elif 'K' in i and 'M' not in i:
        max_v += '5'
        min_v += '5'
    else:
        m_cnt = i.count('M')
        max_v += '1'*m_cnt
        min_v += str(10**(m_cnt-1))

print(max_v)
print(min_v)