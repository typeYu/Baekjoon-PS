# 주의해야 하는 반례
# 5
# 1 2
# 2 5
# 1 3
# 3 4
# 1 2 3 4 5 일 경우
#
# 올바른 탐색 순서는 1 2 3 5 4, 혹은 1 3 2 4 5

import sys
from collections import deque

def bfs():
    visited = [False] * (N + 1)
    visited[1] = 1
    # set()으로 설정하는 이유: bfs()함수에서 현재 노드의 자식을 2, 3으로 구했는데 주어지는 입력값(sequence)에서 3, 2로 나왔을 때 같은 것으로 취급해야 함
    children = [set() for _ in range(N + 1)]
    queue = deque([1])

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                children[node].add(i) # 부모 노드 인덱스 set()에 자식들 노드 번호를 넣어준다.

    return children


N = int(sys.stdin.readline())
graph = [list() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
sequence = list(map(int, sys.stdin.readline().strip().split()))

children = bfs()
next_index = 1 # sequence에서 bfs가 퍼지는 만큼 잘리도록 만드는 변수

for i in sequence:
    if next_index == N:
        break
    c_length = len(children[i])
    # c1: sequence(주어진 순서)에서 현재 노드 i의 자식들
    c1 = set(sequence[next_index:next_index + c_length])
    # c2: bfs를 돌려서 구한 현재 노드 i의 자식들
    c2 = children[i]

    if c1 != c2:
        print(0)
        exit()

    next_index += c_length

print(1)

