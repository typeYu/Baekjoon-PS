def solution(schedules, timelogs, startday):
    l = len(schedules)
    able = [True] * l
    
    for s in range(l): # 허용 시각 구하기
        t, m = int(str(schedules[s])[:-2]), int(str(schedules[s])[-2:])
        t += (m + 10) // 60
        m = (m + 10) % 60
        schedules[s] = [t, m]
    
    for i in range(len(timelogs[0])): # 요일
        if startday in [6, 7]:
            startday = (startday + 1) % 8 if (startday + 1) % 8 != 0 else 1
            continue
        
        for j in range(l): # 사람
            if not able[j]:
                continue
            t, m = schedules[j]
            cur_t, cur_m = int(str(timelogs[j][i])[:-2]), int(str(timelogs[j][i])[-2:])
        
            if t < cur_t or (t == cur_t and m < cur_m):
                able[j] = False
        
        startday = (startday + 1) % 8 if (startday + 1) % 8 != 0 else 1
        
    answer = 0
    for a in able:
        if a:
            answer += 1
    return answer