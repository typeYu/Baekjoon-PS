# 나중에 다시 풀기
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    degree[a] += 1
    degree[b] += 1

q = deque()

# 1. 연결 개수가 1인 노드(리프)는 절대 사이클에 포함될 수 없음 → 큐에 넣기
for i in range(1, n+1):
    if degree[i] == 1:
        q.append(i)

# 2. 리프 제거를 반복하면서 사이클에 포함되지 않는 노드들을 제거
while q:
    cur = q.popleft()
    degree[cur] = 0  # 제거 처리

    for nxt in graph[cur]:
        if degree[nxt] > 0:
            degree[nxt] -= 1
            if degree[nxt] == 1:
                q.append(nxt)

# 3. degree > 0 인 노드들이 순환선
#    이제 BFS로 순환선까지의 거리 계산
dist = [-1] * (n+1)
q = deque()

for i in range(1, n+1):
    if degree[i] > 0:      # 순환선 노드
        dist[i] = 0
        q.append(i)

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

print(*dist[1:])
