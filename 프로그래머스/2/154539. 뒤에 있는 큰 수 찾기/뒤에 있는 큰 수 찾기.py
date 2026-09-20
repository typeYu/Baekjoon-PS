def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, num in enumerate(numbers):
        while len(stack) > 0:
            if stack[-1][1] < num:
                ii, _ = stack.pop()
                answer[ii] = num
            else:
                break
        
        stack.append([i, num])
    
    return answer