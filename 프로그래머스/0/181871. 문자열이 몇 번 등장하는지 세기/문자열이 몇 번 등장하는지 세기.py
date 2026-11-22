def solution(myString, pat):
    answer = 0
    pl = len(pat)
    for i in range(len(myString) - pl + 1):
        if pat == myString[i:i + pl]:
            answer += 1
    
    return answer