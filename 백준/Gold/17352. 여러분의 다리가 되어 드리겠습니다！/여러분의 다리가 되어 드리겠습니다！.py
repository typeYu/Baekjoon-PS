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

N = int(sys.stdin.readline())
parent = [i for i in range(N + 1)]
for _ in range(N - 2):
    node1, node2 = map(int, sys.stdin.readline().strip().split())
    union_parents(node1, node2)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            continue
        i_p = find_parnets(i)
        j_p = find_parnets(j)

        if i_p != j_p:
            print(i, j)
            exit()
        