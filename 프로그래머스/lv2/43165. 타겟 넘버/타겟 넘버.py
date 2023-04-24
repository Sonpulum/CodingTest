def solution(numbers, target):
    answer = 0
    l = len(numbers)
    
    stack = []
    stack.append((-numbers[0],0))
    stack.append((numbers[0],0))
    
    while stack:
        e, c = stack.pop()
        if c+1 == l:
            if e == target:
                answer += 1
                          
        elif c+1 < l:
            for i in (-numbers[c+1], numbers[c+1]):
                n = e+i
                stack.append((n,c+1))
                
    
    return answer