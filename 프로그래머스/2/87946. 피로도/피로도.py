from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for per in permutations(dungeons):
        ans = 0
        fatigue = k
        for minimum, need in per:
            if fatigue >= minimum:
                fatigue -= need
                ans += 1
        answer = max(answer, ans)
    
    return answer