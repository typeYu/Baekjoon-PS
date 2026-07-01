def solution(topping):
    dic1, dic2 = {topping[0] : 1}, dict()
    for t in topping[1:]:
        if t in dic2:
            dic2[t] += 1
        else:
            dic2[t] = 1
    
    if len(dic1) == len(dic2):
        answer = 1
    else:
        answer = 0
    
    for i in range(1, len(topping)):
        t = topping[i]
        if t in dic1:
            dic1[t] += 1
        else:
            dic1[t] = 1
        
        if dic2[t] == 1:
            dic2.pop(t)
        else:
            dic2[t] -= 1
        
        if len(dic1) == len(dic2):
            answer += 1
    
    return answer
        