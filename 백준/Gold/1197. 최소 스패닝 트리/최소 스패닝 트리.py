# 크루스칼 알고리즘
import sys
sys.setrecursionlimit(100000)
V, E = map(int, sys.stdin.readline().strip().split())
graph = []
parent = [i for i in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    graph.append([C, A, B])

graph.sort()

# 집합의 부모 노드를 찾는 함수
def find_parent(a):
    global parent
    # 만약 a의 부모가 다른 노드라면
    if parent[a] != a:
        # parent 배열에 부모 노드를 기록한다
        parent[a] = find_parent(parent[a]) # 경로 압축 해야 시간복잡도 줄음
    # 부모 노드 반환
    return parent[a]

def union(a, b):
    ap = find_parent(a)
    bp = find_parent(b)
    if ap > bp:
        parent[ap] = bp
    else:
        parent[bp] = ap

total = 0
for cost, a, b in graph:
    if find_parent(a) != find_parent(b): # 부모 노드가 같으면 사이클 발생
        union(a, b)
        total += cost

print(total)