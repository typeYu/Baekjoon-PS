from collections import deque
import sys
input = sys.stdin.readline
 
f, s, g, u, d = map(int, input().split())
visited = [-1] * (f + 1)
 
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0
 
    while q:
        cur = q.popleft()
 
        if cur == g:
            return visited[cur]
 
        for next in (cur + u, cur - d):
            if 0 < next <= f and visited[next] == -1:
                visited[next] = visited[cur] + 1
                q.append(next)
                
    # G까지 도달하지 못할 경우
    if visited[g] == -1: 
        return "use the stairs"
 
print(bfs(s))