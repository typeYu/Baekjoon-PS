def solution(skill, skill_trees):
    dic = dict() # 문자열: 숫자
    for i in range(len(skill)):
        dic[skill[i]] = i
    
    answer = 0
    for s in skill_trees:
        visited = [False] * len(skill)
        vert = 0
        for ss in s:
            if ss in dic and dic[ss] == 0:
                visited[0] = True
                vert += 1
            elif ss in dic:
                if visited[dic[ss] - 1]:
                    vert += 1
                    visited[dic[ss]] = True
                else:
                    break
            else:
                vert += 1
        
        if vert == len(s):
            answer += 1
    
    return answer
        
        