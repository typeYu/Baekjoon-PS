def solution(k, score):
    answer, stack = [], []
    for s in score:
        stack.append(s)
        stack.sort(reverse=True)
        if len(stack) > k:
            stack.pop()
        answer.append(stack[-1])
    
    return answer