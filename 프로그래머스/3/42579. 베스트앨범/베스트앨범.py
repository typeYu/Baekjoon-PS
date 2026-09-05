def solution(genres, plays):
    dic = {}
    dic_cnt = {}
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        
        if g not in dic:
            dic[g] = [[p, i]]
            dic_cnt[g] = plays[i]
        else:
            dic[g].append([p, i])
            dic_cnt[g] += plays[i]
    
    for d in dic.values():
        d.sort(key=lambda x: (-x[0], x[1]))
    
    sorted_dic_cnt = dict(sorted(dic_cnt.items(), key=lambda x: -x[1]))
    
    answer = []
    for d in sorted_dic_cnt:
        answer.append(dic[d][0][1])
        if len(dic[d]) > 1:
            answer.append(dic[d][1][1])
    
    return answer