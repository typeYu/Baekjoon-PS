from collections import deque
def solution(queue1, queue2):
    q1, q2 = sum(queue1), sum(queue2)
    l = len(queue1) + len(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)
    cnt = 0
    
    while cnt < l * 2:
        if q1 == q2:
            return cnt
        elif q1 > q2:
            q = queue1.popleft()
            q1 -= q
            queue2.append(q)
            q2 += q
        else:
            q = queue2.popleft()
            q2 -= q
            queue1.append(q)
            q1 += q
        cnt += 1
    
    return -1
        