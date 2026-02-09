def solution(n):
    # 배열 선언
    answer = []
    for i in range(1, n + 1):
        arr = []
        for j in range(i):
            arr.append(0)
        answer.append(arr)
    
    # 숫자 최대 크기 계산
    max_num, num = 0, 1
    for i in range(1, n + 1):
        max_num += i
    
    # 배열 채우기
    y, x, d = 0, 0, 0
    dy = [1, 0, -1]
    dx = [0, 1, -1]
    
    while (num <= max_num):
        answer[y][x] = num
        if 0 <= y + dy[d] < n and 0 <= x + dx[d] < n and answer[y + dy[d]][x + dx[d]] == 0:
            y += dy[d]
            x += dx[d]
        else:
            d = (d + 1) % 3
            y += dy[d]
            x += dx[d]
        
        num += 1

    real_answer = answer[0]
    for s in range(1, len(answer)):
        real_answer += answer[s]
    
    return real_answer
