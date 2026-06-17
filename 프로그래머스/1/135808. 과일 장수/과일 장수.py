def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        if len(score[i:i + m]) >= m:
            answer += m * min(score[i:i + m])
    return answer