import sys


def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])

    return parent[a]


def union(a, b):
    a_p = find_parent(a)
    b_p = find_parent(b)

    if a_p != b_p:
        if a_p < b_p:
            parent[b_p] = a_p
        else:
            parent[a_p] = b_p


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
parent = [i for i in range(G + 1)]
answer = 0

for _ in range(P):
    i = int(sys.stdin.readline())

    i_parent = find_parent(i)
    if i_parent == 0:
        break
    else:
        union(i_parent, i_parent - 1)
        answer += 1

print(answer)