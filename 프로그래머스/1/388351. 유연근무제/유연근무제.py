def solution(schedules, timelogs, startday):
    l = len(schedules)
    people = [True] * l
    
    for i in range(l):
        hour = schedules[i] // 100
        minute = schedules[i] % 100 + 10

        if minute >= 60:
            hour += 1
            minute -= 60

        time_limit = hour * 100 + minute
        s = startday
        
        for t in timelogs[i]:
            print(f"i:{i}, s:{s}, t:{t}, time_limit:{time_limit}")
            if s != 6 and s != 7:
                if t > time_limit:
                    print(f"False: i:{i} s:{s} t:{t}, time_limit:{time_limit}")
                    people[i] = False
                    break
            s = 1 if s == 7 else s + 1
        
    return people.count(True)