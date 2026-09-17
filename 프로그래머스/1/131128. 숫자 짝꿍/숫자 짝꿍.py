def solution(X, Y):
    dic1, dic2 = dict(), dict()
    until = set()
    
    for num in list(map(int, X)):
        if num in dic1:
            dic1[num] += 1
        else:
            dic1[num] = 1
        
        until.add(num)
    
    for num in list(map(int, Y)):
        if num in dic2:
            dic2[num] += 1
        else:
            dic2[num] = 1
    
        until.add(num)
    
    answer = []
    for num in until:
        if num in dic1 and num in dic2:
            for _ in range(min(dic1[num], dic2[num])):
                answer.append(num)
    
    answer.sort(reverse=True)
    ans = ''.join(map(str, answer))
    if ans == '':
        return '-1'
    elif ans[0] == '0' and len(ans) > 1:
        return '0'
    else:
        return ans
    