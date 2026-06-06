def solution(keymap, targets):
    dic = {}
    for k in keymap:
        for i in range(len(k)):
            if k[i] in dic:
                dic[k[i]] = min(i, dic[k[i]])
            else:
                dic[k[i]] = i
    
    answer = []
    for i in range(len(targets)):
        ans = 0
        for s in targets[i]:
            if s in dic:
                ans += dic[s] + 1
            else:
                ans = -1
                break
        answer.append(ans)
    
    return answer