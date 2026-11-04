def solution(today, terms, privacies):
    today_y, today_m, today_d = today.split('.')
    today_y, today_m, today_d = int(today_y) - 2000, int(today_m) * 28, int(today_d)
    today = today_y * 12 * 28 + today_m + today_d # 오늘 날짜
    
    dic = {}
    for t in terms:
        s, m = t.split(' ')
        dic[s] = int(m)
    
    answer = []
    for i in range(len(privacies)):
        date, s = privacies[i].split(' ')
        y, m, d = date.split('.')
        y, m, d = int(y) - 2000, int(m) * 28, int(d)
        date = y * 12 * 28 + m + d + dic[s] * 28 # 유효기간
    
        if date <= today: # 유효기간이 오늘 날짜보다 더 작다면 파기
            answer.append(i + 1)
    
    return answer