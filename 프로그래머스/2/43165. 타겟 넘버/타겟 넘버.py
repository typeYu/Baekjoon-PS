def solution(numbers, target):
    answer = 0
    
    def dfs(n, t):
        nonlocal answer
        
        if n == len(numbers):
            if t == target:
                answer += 1
            return
        
        for i in [numbers[n], -numbers[n]]:
            dfs(n + 1, t + i)
            
    
    dfs(0, 0)
    return answer