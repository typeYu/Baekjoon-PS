def solution(record):
    dic = dict()
    for r in record:
        parts = r.split()
        command, uid = parts[:2]

        if command != "Leave":
            nickname = parts[2]
        
            dic[uid] = nickname
        
    # 진짜 계산
    answer = []
    for r in record:
        parts = r.split()
        command, uid = parts[:2]
        
        if command == 'Enter':
            answer.append(f"{dic[uid]}님이 들어왔습니다.")
        elif command == 'Leave':
            answer.append(f"{dic[uid]}님이 나갔습니다.")
    
    return answer
        