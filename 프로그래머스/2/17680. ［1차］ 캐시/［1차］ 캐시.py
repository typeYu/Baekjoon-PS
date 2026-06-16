def solution(cacheSize, cities):
    answer = 0
    queue = []
    for c in cities:
        C = c.upper()
        if C in queue:
            queue.remove(C)
            answer += 1
        else:
            answer += 5
        queue.append(C)
        
        if len(queue) > cacheSize:
            queue.pop(0)
    
    return answer