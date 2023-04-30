while True:
    flag = 1
    s = input()

    if s == '.':
        flag = 0
        break

    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    flag = 0
                    break
            else:
                flag = 0
                break

        elif i == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    flag = 0
                    break
            else:
                flag = 0
                break
    if stack:
        flag = 0

    if flag:
        print('yes')
    else:
        print('no')