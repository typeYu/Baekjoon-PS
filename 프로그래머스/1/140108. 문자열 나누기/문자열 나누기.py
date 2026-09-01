def solution(s):
    answer = 1
    s = list(s)
    is_last = False
    while len(s) > 0:
        a = s[0]
        a_cnt, another_cnt = 1, 0
        if len(s) == 1:
            break
        for i in range(1, len(s)):
            if i == len(s) - 1:
                is_last = True
                break
            
            if s[i] == a:
                a_cnt += 1
            else:
                another_cnt += 1
            
            if a_cnt == another_cnt:
                answer += 1
                s = s[a_cnt + another_cnt:]
                break
        
        if is_last:
            break
        
    return answer