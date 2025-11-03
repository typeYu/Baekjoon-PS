import sys
import heapq

def topology_sort():
    answer = []
    queue = []
    for i in range(1, N + 1):
        if inDegree[i] == 0:
            heapq.heappush(queue, i)
    
    while queue:
        people = heapq.heappop(queue)
        answer.append(people)
        for j in child[people]:
            inDegree[j] -= 1
            if inDegree[j] == 0: # 이 부분 왜 기억을 못했지
                heapq.heappush(queue, j)
            
    return answer


N, M = map(int, sys.stdin.readline().strip().split())
child = [list() for _ in range(N + 1)]
inDegree = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    inDegree[b] += 1
    child[a].append(b)
    
print(*topology_sort())