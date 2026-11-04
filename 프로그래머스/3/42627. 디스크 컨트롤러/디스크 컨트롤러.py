import heapq

def solution(jobs):
    l = len(jobs)
    queue, wait = [], [] # 힙 돌릴 큐, 시간 순으로 정렬할 배열
    for i in range(l):
        start, end = jobs[i]
        if start == 0:
            heapq.heappush(queue, [end, start, i])
        else:
            wait.append([end, start, i])
    
    wait.sort(reverse=True, key=lambda x: x[1])
    
    times = 0
    answer = 0
    while queue or wait:
        # 만약 시간 순으로 정렬한 배열 끝에 작업 시작할 수 있는 작업이 있으면 queue에 넣어줌
        while wait:
            if wait[-1][1] <= times:
                w = wait.pop()
                heapq.heappush(queue, w)
            else:
                break
        
        # queue에서 시작할 수 있는 작업이 없으면 시간을 증가시켜줘야 함
        if not queue:
            times += 1
            continue
        
        # queue에서 소요시간, 작업 요청 시각, 번호 순으로 제일 우선순위가 높은 작업을 heap으로 뽑음
        t, s, i = heapq.heappop(queue)
        times += t
        answer += times - s
    
    return answer // l
        