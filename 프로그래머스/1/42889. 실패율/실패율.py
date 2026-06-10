def solution(N, stages):
    dic = {i:0 for i in range(N + 2)} # N + 2인 이유: 이 문제는 N(스테이지)가 5일 때 완주자인 6이 들어올 수 있음
    for num in stages:
        dic[num] += 1
    
    answer = []
    stages_total = len(stages)
    for i in range(1, N + 1):
        stages_total -= dic[i - 1]
        
        if stages_total == 0:
            reach = 0
        else:
            reach = dic[i] / stages_total
        answer.append([reach, i])
    
    answer.sort(key=lambda x: (-x[0], x[1]))    
        
    return [i[1] for i in answer]