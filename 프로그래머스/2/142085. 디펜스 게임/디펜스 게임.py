import heapq
def solution(n, k, enemy):
    K = k
    answer = 0
    queue = []
    for e in enemy:
        if len(queue) < K and 0 < k:
            k -= 1
            heapq.heappush(queue, e)
        elif len(queue) == K:
            q = heapq.heappop(queue)
            if q < e:
                n -= q
                heapq.heappush(queue, e)
            else:
                n -= e
                heapq.heappush(queue, q)
        
        if n < 0:
            break
        
        answer += 1
    
    return answer
        