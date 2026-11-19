def solution(weights):
    dic = dict()
    for w in weights:
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1
    
    weights.sort()
    
    answer = 0
    for w in weights:
        answer += dic[w] - 1
        
        if w % 2 == 0 and (w // 2) * 3 in dic:
            answer += dic[(w // 2) * 3]
            
        if w % 3 == 0 and (w // 3) * 4 in dic:
            answer += dic[(w // 3) * 4]
        
        if w * 2 in dic:
            answer += dic[w * 2]
        
        dic[w] -= 1

    return answer