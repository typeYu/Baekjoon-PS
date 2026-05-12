import math

def solution(progresses, speeds):
    stack = []
    for i in range(len(progresses)):
        stack.append(math.ceil((100 - progresses[i]) / speeds[i]))

    answer = []
    cnt = 1
    start = stack[0]
    for i in range(1, len(progresses)):
        if start < stack[i]:
            answer.append(cnt)
            start = stack[i]
            cnt = 1
        else:
            cnt += 1
    
    answer.append(cnt)
    
    return answer