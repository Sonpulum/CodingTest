def solution(nums):
    answer = 0
    pokemons = {}
    n = len(nums)
    for i in nums:
        if i in pokemons:
            pokemons[i] += 1
        else:
            pokemons[i] = 1
    k = len(list(pokemons.keys()))
    
    if k > n//2:
        answer = n//2
    else:
        answer = k
        
    return answer