def solution(routes):
    routes.sort(key=lambda x: x[1])
    
    answer = 0
    cur = float('inf')
    for s, e in routes:
        if s > cur or cur > e:
            cur = e
            answer += 1

    return answer