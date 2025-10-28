import sys


def move(graph, cnt):
    global answer

    if cnt == 5:
        for g in graph:
            answer = max(max(g), answer)
        return

    for i in range(4):
        if i == 0:
            move(up(graph), cnt + 1)
        elif i == 1:
            move(down(graph), cnt + 1)
        elif i == 2:
            move(left(graph), cnt + 1)
        else:
            move(right(graph), cnt + 1)


def up(graph):
    new_graph = [[0] * N for _ in range(N)]
    for i in range(N):
        stack = [graph[0][i]] if graph[0][i] != 0 else []
        is_merged = False
        for j in range(1, N):
            if graph[j][i]: # j, i에 숫자가 있으면
                if stack and stack[-1] == graph[j][i] and not is_merged: # 만약 합칠 수 있다면
                    stack.pop()
                    stack.append(graph[j][i] * 2)
                    is_merged = True
                else:
                    is_merged = False
                    stack.append(graph[j][i])

        for idx in range(len(stack)):
            new_graph[idx][i] = stack[idx]

    return new_graph


def down(graph):
    new_graph = [[0] * N for _ in range(N)]
    for i in range(N):
        stack = [graph[N - 1][i]] if graph[N - 1][i] != 0 else []
        is_merged = False
        for j in range(N - 2, -1, -1):
            if graph[j][i]:
                if stack and stack[-1] == graph[j][i] and not is_merged:  # 만약 합칠 수 있다면
                    stack.pop()
                    stack.append(graph[j][i] * 2)
                    is_merged = True
                else:
                    is_merged = False
                    stack.append(graph[j][i])

        stack_idx = 0
        for idx in range(N - 1, N - 1 - len(stack), -1):
            new_graph[idx][i] = stack[stack_idx]
            stack_idx += 1

    return new_graph


def left(graph):
    new_graph = [[0] * N for _ in range(N)]
    for i in range(N):
        stack = [graph[i][0]] if graph[i][0] != 0 else []
        is_merged = False
        for j in range(1, N):
            if graph[i][j]:
                if stack and stack[-1] == graph[i][j] and not is_merged:
                    stack.pop()
                    stack.append(graph[i][j] * 2)
                    is_merged = True
                else:
                    is_merged = False
                    stack.append(graph[i][j])

        for idx in range(len(stack)):
            new_graph[i][idx] = stack[idx]

    return new_graph


def right(graph):
    new_graph = [[0] * N for _ in range(N)]
    for i in range(N):
        stack = [graph[i][N - 1]] if graph[i][N - 1] != 0 else []
        is_merged = False
        for j in range(N - 2, -1, -1):
            if graph[i][j]:
                if stack and stack[-1] == graph[i][j] and not is_merged:
                    stack.pop()
                    stack.append(graph[i][j] * 2)
                    is_merged = True
                else:
                    is_merged = False
                    stack.append(graph[i][j])

        stack_idx = 0
        for idx in range(N - 1, N - 1 - len(stack), -1):
            new_graph[i][idx] = stack[stack_idx]
            stack_idx += 1

    return new_graph


N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
answer = 0

move(graph, 0)
print(answer)