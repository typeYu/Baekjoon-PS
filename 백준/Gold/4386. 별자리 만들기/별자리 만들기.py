import sys


def find_parents(a):
    if parents[a] != a:
        parents[a] = find_parents(parents[a])

    return parents[a]


def union(a, b):
    a_p = find_parents(a)
    b_p = find_parents(b)

    if a_p != b_p:
        if a_p < b_p:
            parents[b_p] = a_p
        else:
            parents[a_p] = b_p


n = int(sys.stdin.readline())
parents = [i for i in range(n)]
stars = []
distance_gather = []
for node in range(n):
    x, y = map(float, sys.stdin.readline().strip().split())
    stars.append([x, y])
    for i in range(node):
        x2, y2 = stars[i][0], stars[i][1]
        distance = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
        distance_gather.append([node, i, distance])


distance_gather.sort(key=lambda x: x[2])

answer = 0
for a, b, dist in distance_gather:
    if find_parents(a) != find_parents(b):
        union(a, b)
        answer += dist

print(round(answer, 2))