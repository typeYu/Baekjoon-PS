import sys

def find_parent(node):
    if node != parent[node]:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union_parent(i, j):
    p_i = find_parent(i)
    p_j = find_parent(j)

    if p_i != p_j:
        if p_i < p_j:
            parent[p_j] = p_i
            size[p_i] += size[p_j]
        else:
            parent[p_i] = p_j
            size[p_j] += size[p_i]

N, Q = map(int, sys.stdin.readline().strip().split())
graph = []
parent = [i for i in range(N + 1)]
kv = []
size = [1] * (N + 1) # 유니온파인드 후 연결 노드 기록
answer = [0] * Q # 답 기록 후 한번에 출력 할 배열

for _ in range(N - 1):
    p, q, r = map(int, sys.stdin.readline().strip().split())
    graph.append((p, q, r))

for i in range(Q):
    k, v = map(int, sys.stdin.readline().strip().split())
    kv.append((k, v, i))

graph.sort(key=lambda x: x[2], reverse=True)
kv.sort(key=lambda x: x[0], reverse=True)

idx = 0
for k, v, i in kv:
    # 유사도 높은 순서대로 유니온 하면서 answer 늘려야
    while idx < N - 1 and graph[idx][2] >= k:
        p, q, r = graph[idx]
        union_parent(p, q)
        idx += 1
    answer[i] = size[find_parent(v)] - 1

for a in answer:
    print(a)