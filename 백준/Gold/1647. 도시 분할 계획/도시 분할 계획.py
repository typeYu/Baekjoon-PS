import sys
N, M = map(int, sys.stdin.readline().strip().split())
graph = []
parent = [i for i in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    graph.append([C, A, B]) # 간선을 중심으로 저장
graph.sort() # 간선 가중치를 기준으로 정렬

def find_parent(a):
    global parent
    if parent[a] != a: # a의 집합의 부모가 a가 아니라면
        parent[a] = find_parent(parent[a]) # 경로 압축: a의 부모 기록
    return parent[a] # 부모 노드 리턴

def union(a, b):
    ap = find_parent(a) # 부모 기준으로 묶어야 사이클 미발생
    bp = find_parent(b)
    if ap > bp:
        parent[ap] = bp
    else:
        parent[bp] = ap

result = 0
max_cost = 0
for cost, a, b in graph:
    if find_parent(a) != find_parent(b): # 부모 노드가 같지 않아야 사이클 미 발생, 사이클이 없어야 크루스칼 알고리즘 성립
        union(a, b)
        result += cost
        max_cost = max(max_cost, cost)

print(result - max_cost)
