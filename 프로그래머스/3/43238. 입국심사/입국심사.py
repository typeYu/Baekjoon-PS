def solution(n, times):
    start, end = 1, max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        
        done = 0
        for t in times:
            done += mid // t
        
        # 이번 mid시간에 일을 끝마친 사람 done이 끝마쳐야 하는 사람 수 n보다 작다면 mid를 늘려준다
        if done < n:
            start = mid + 1
        # 이번 mid시간에 일을 끝마친 사람 done이 끝마쳐야 하는 사람 수 n보다 크거나 같다면 mid를 줄여준다
        else:
            end = mid - 1
    
    return start