from collections import deque
n = int(input())
array = [list() for _ in range(26)]
for _ in range(n):
    S = input().split(' ')
    a = ord(S[0]) - ord('a')
    b = ord(S[2]) - ord('a')
    array[a].append(b)


def bfs(start, end):
    visited = [False] * 26
    queue = deque([start])
    visited[start] = True

    while queue:
        q = queue.popleft()
        if q == end:
            return True
        for d in array[q]:
            if not visited[d]:
                visited[d] = True
                queue.append(d)
    return False


m = int(input())
for _ in range(m):
    S = input().split()
    a = ord(S[0]) - ord('a')
    b = ord(S[2]) - ord('a')
    if bfs(a, b):
        print("T")
    else:
        print("F")