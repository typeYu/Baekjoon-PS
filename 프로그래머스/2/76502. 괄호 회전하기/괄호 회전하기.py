from collections import deque
def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        s.rotate(-1)
        stack = []
        for ss in s:
            is_right = True
            if len(stack) == 0 and ss in [')', ']', '}']:
                is_right = False
                break
            elif ss == ')' and stack[-1] == '(':
                stack.pop()
            elif ss == ']' and stack[-1] == '[':
                stack.pop()
            elif ss == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(ss)
        if is_right and len(stack) == 0:
            answer += 1
    
    return answer
    