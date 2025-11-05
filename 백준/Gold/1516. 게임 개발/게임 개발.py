import sys
from collections import deque


def topology_sort():
    answer = [0] * (N + 1)
    queue = deque()
    for i in range(1, N + 1):
        if inDegree[i] == 0:
            queue.append(i)
            answer[i] = time[i]

    while queue:
        building = queue.popleft()
        for next in child[building]:
            inDegree[next] -= 1
            if inDegree[next] == 0:
                queue.append(next) # 위상정렬 시 inDegree가 0이어야 큐에 들어감
                answer[next] = time[next]
                max_time = 0
                for p in parent[next]:
                    max_time = max(max_time, answer[p]) # 인덱스 오류 주의
                answer[next] += max_time

    return answer

N = int(sys.stdin.readline())
child = [list() for _ in range(N + 1)]
parent = [list() for _ in range(N + 1)]
inDegree = [0] * (N + 1)
time = [0]

for i in range(1, N + 1):
    array = list(map(int, sys.stdin.readline().strip().split()))
    time.append(array[0])
    if array[1] != -1:
        for before in range(1, len(array) - 1):
            child[array[before]].append(i)
            parent[i].append(array[before])
            inDegree[i] += 1

print(*topology_sort()[1:], sep ='\n')

