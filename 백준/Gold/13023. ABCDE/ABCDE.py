import sys
sys.setrecursionlimit(10**5) # 재귀깊이 에러, 메모리 초과 피하기(10**6: 메모리초과)

N, M = map(int, sys.stdin.readline().strip().split())
graph = [list() for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node, visited, cnt):
    global result
    if cnt == 5:
        print(1)
        exit() # 시간 초과 피하기

    for j in graph[node]:
        if j not in visited:
            visited.append(j)
            dfs(j, visited, cnt + 1)
            visited.pop()

result = 0
for i in range(N):
    dfs(i, [i], 1)

print(result)