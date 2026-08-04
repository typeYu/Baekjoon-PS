def solution(n, m, section):
    answer = 0
    painted = 0
    for i in range(len(section)):
        if section[i] > painted:
            answer += 1
            painted = section[i] + m - 1
    
    return answer