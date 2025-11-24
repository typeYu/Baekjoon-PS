import sys


def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union_parent(a, b):
    a_p = find_parent(a)
    b_p = find_parent(b)

    if a_p != b_p:
        if a_p > b_p:
            parent[b_p] = a_p
        else:
            parent[a_p] = b_p


N = int(sys.stdin.readline())
parent = [i for i in range(N)]
planets = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().strip().split())
    planets.append([x, y, z, i])

edges = []

# x축 정렬해서 나오는 비용(min(|xA-xB|, |yA-yB|, |zA-zB|))
planets.sort(key = lambda x: x[0])
for i in range(N-1):
    a = planets[i][3]
    b = planets[i+1][3]
    cost = abs(planets[i][0] - planets[i+1][0])
    edges.append([a, b, cost])

# y축 정렬
planets.sort(key = lambda x: x[1])
for i in range(N-1):
    a = planets[i][3]
    b = planets[i+1][3]
    cost = abs(planets[i][1] - planets[i+1][1])
    edges.append([a, b, cost])

# x축 정렬
planets.sort(key = lambda x: x[2])
for i in range(N-1):
    a = planets[i][3]
    b = planets[i+1][3]
    cost = abs(planets[i][2] - planets[i+1][2])
    edges.append([a, b, cost])

edges.sort(key = lambda x: x[2])
answer = 0

for a, b, cost in edges:
    a_p = find_parent(a)
    b_p = find_parent(b)
    
    if a_p != b_p:
        union_parent(a, b)
        answer += cost

print(answer)