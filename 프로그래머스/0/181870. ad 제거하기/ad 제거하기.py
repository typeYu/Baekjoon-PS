def solution(strArr):
    result = [] 
    for i in strArr: 
        if 'ad' not in i: result.append(i)
    return result