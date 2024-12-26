import sys
sys.setrecursionlimit(100001)


def dfs(num):
    global answer, group

    if not visited[array[num]]:
        group.append(array[num])
        visited[array[num]] = True
        dfs(array[num])
    elif array[array[num]] in group:
        answer += len(group[group.index(array[num]):])
        group = []


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    array = [0] + list(map(int, sys.stdin.readline().strip().split()))
    visited = [False] * (N + 1)
    answer = 0
    for i in range(1, N + 1):
        if not visited[i]:
            group = [i]
            visited[i] = True
            dfs(i)
    print(N - answer)