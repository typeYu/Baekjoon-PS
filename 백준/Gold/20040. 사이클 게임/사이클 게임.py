import sys

def find_parent(a):
    global parent
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a, b):
    ap = find_parent(a)
    bp = find_parent(b)
    if ap > bp:
        parent[ap] = bp
    else:
        parent[bp] = ap

n, m = map(int, sys.stdin.readline().strip().split())
graph, parent = [], [i for i in range(n + 1)]
for idx in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    if find_parent(a) == find_parent(b):
        print(idx)
        exit()
    union(a, b)
print(0)
