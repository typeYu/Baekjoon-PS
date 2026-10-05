from collections import deque
def solution(n, wires):
    answer = float('inf')
    
    def bfs(lists):
        nonlocal answer
        graph = [list() for _ in range(n + 1)]
        visited = [False] * (n + 1)
        for v1, v2 in lists:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        gap = 0
        for node in range(1, n + 1):
            if not visited[node]:
                ans = 1
                queue = deque([node])
                visited[node] = True
                while queue:
                    q = queue.popleft()
                    for qq in graph[q]:
                        if not visited[qq]:
                            visited[qq] = True
                            queue.append(qq)
                            ans += 1
                gap = abs(gap - ans)
        return gap
    
    l = len(wires)
    for i in range(l):
        lists = []
        for j in range(l):
            if i == j:
                continue
            lists.append(wires[j])
        answer = min(answer, bfs(lists))
    
    return answer
        