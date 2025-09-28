import sys


def find_parents(a):
    if parents[a] != a:
        parents[a] = find_parents(parents[a])
    return parents[a]


def union_parents(a, b):
    a_p = find_parents(a)
    b_p = find_parents(b)

    if a_p != b_p:
        if a_p < b_p:
            parents[b_p] = a_p
        else:
            parents[a_p] = b_p


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parents = [i for i in range(N + 1)]
costs = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    costs.append([c, a, b])

costs.sort(key=lambda x: x[0])
answer = 0

for c, a, b in costs:
    a_p = find_parents(a)
    b_p = find_parents(b)
    if a_p != b_p:
        union_parents(a, b)
        answer += c

print(answer)
