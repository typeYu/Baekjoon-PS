def solution(clothes):
    dic = dict()
    for name, clothes_type in clothes:
        if clothes_type in dic:
            dic[clothes_type].append(name)
        else:
            dic[clothes_type] = [name]
    
    answer = 1
    for val in dic.values():
        answer *= (len(val) + 1)
    
    return answer - 1
    