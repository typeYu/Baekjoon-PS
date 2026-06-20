def solution(want, number, discount):
    answer = 0
    dic = dict()
    arr = discount[:10]
    for a in arr:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    
    for w in range(len(want)):
        if want[w] not in dic:
            break
        elif want[w] in dic and number[w] > dic[want[w]]:
            break
    else:
        answer += 1
        
    
    for i in range(len(discount) - 10):
        dic[discount[i]] -= 1
        if discount[i + 10] in dic:
            dic[discount[i + 10]] += 1
        else:
            dic[discount[i + 10]] = 1
        
        for w in range(len(want)):
            if want[w] not in dic:
                break
            elif want[w] in dic and number[w] > dic[want[w]]:
                break
        else:
            answer += 1
    
    return answer