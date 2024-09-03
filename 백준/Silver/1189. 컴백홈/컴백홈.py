R, C, K = map(int, input().split())
graph = [list(input()) for _ in range(R)]
graph[R - 1][0] = 'T'

result = 0
def backtracking(length, y, x):
    global result
    if y == 0 and x == C - 1 and length == K:
        result += 1
    else:
        for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= y + i < R and 0 <= x + j < C and graph[y + i][x + j] != 'T':
                    graph[y + i][x + j] = 'T'
                    backtracking(length + 1, y + i, x + j)
                    graph[y + i][x + j] = '.'


backtracking(1, R - 1, 0)
print(result)