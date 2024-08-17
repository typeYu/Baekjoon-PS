from collections import deque
def solution(n, computers):
    visited = [False] * n
    
    def bfs(num):
        queue = deque([num])
        visited[num] = True
        
        while queue:
            num = queue.popleft()
            for i in range(len(computers[num])):
                if i == num:
                    continue
                elif computers[num][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
        
    return answer