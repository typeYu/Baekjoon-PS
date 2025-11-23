import sys


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union_parent(x, y):
    x_p = find_parent(x)
    y_p = find_parent(y)

    if x_p != y_p:
        if x_p < y_p:
            parent[y_p] = x_p
        else:
            parent[x_p] = y_p


while True:
    m, n = map(int, sys.stdin.readline().strip().split())
    if m == 0 and n == 0:
        break
    graph, parent = [], [i for i in range(m)]
    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().strip().split())
        graph.append([z, x, y])

    graph.sort(key=lambda x: x[0])
    answer = 0

    for z, x, y in graph:
        if find_parent(x) != find_parent(y):
            union_parent(x, y)
        else:
            answer += z # 이 문제는 불 켜져 있는 길 비용을 구하는게 아니라 불 꺼진 길 비용을 구하는 것임

    print(answer)