import sys

def find_parnets(a):
    if a != parent[a]:
        parent[a] = find_parnets(parent[a])

    return parent[a]

def union_parents(a, b):
    a_p = find_parnets(a)
    b_p = find_parnets(b)

    if a_p != b_p:
        if a_p < b_p:
            parent[b_p] = find_parnets(a_p)
        else:
            parent[a_p] = find_parnets(b_p)


N, M = map(int, sys.stdin.readline().strip().split())                       
parent = [i for i in range(N + 1)]
nodes = []
for num in range(1, N + 1):
    X, Y = map(int, sys.stdin.readline().strip().split())
    nodes.append([num, X, Y])

distance_between = []
for i in range(len(nodes)):
    for j in range(i, len(nodes)):
        if i == j:
            continue
        distance = ((nodes[i][1] - nodes[j][1]) ** 2 + (nodes[i][2] - nodes[j][2]) ** 2) ** 0.5
        distance_between.append([distance, nodes[i][0], nodes[j][0]])

for _ in range(M):
    X, Y = map(int, sys.stdin.readline().strip().split())
    x_p = find_parnets(X)
    y_p = find_parnets(Y)

    if x_p != y_p:
        union_parents(x_p, y_p)

distance_between.sort(key = lambda x: x[0])

answer = 0
for i in range(len(distance_between)):
    node1, node2 = distance_between[i][1], distance_between[i][2]
    distance = distance_between[i][0]

    node1_p = find_parnets(node1)
    node2_p = find_parnets(node2)
    if node1_p != node2_p:
        union_parents(node1, node2)
        answer += distance

print(f"{answer:.2f}")