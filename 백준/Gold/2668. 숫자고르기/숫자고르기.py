# dfs로 깊이 들어가다가 사이클 생기면 만들어주는 걸로 할까

import sys


def dfs(cur, S):
    global visited, answer

    if arr[cur] in S:
        S = list(S)
        answer += S[S.index(arr[cur]):]
        answer.append(cur)
        return

    if not visited[arr[cur]]:
        visited[arr[cur]] = True
        S.add(cur)
        dfs(arr[cur], S)
        S.pop()


N = int(sys.stdin.readline())
arr = [0]
for _ in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)

visited = [False] * (N + 1)
answer = []

for i in range(1, N + 1):
    visited[i] = True
    dfs(i, {i})

answer.sort()
answer = set(answer)
print(len(answer))
print(*answer, sep='\n')