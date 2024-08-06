import sys
from collections import deque
case = 1
while True:
    N = int(input())
    if N == 0:
        break

    graph, visited, setN = {}, {}, set()
    for i in range(N):
        people1, people2 = sys.stdin.readline().strip().split()
        graph[people1] = people2
        visited[people1] = False
        visited[people2] = False
        setN.add(people1)
        setN.add(people2)

    def bfs(S):
        queue = deque([S])
        visited[S] = True

        while queue:
            S = queue.popleft()
            NS = graph[S]
            if not visited[NS]:
                visited[NS] = True
                queue.append(NS)

    count = 0
    for i in setN:
        if not visited[i]:
            bfs(i)
            count += 1

    print(case, count)
    case += 1