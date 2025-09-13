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


case = 1
while True:
    n, m = map(int, sys.stdin.readline().strip().split())
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]
    not_tree = set()

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        a_p = find_parnets(a)
        b_p = find_parnets(b)
        if a_p != b_p:
            union_parents(a, b)
        else:
            not_tree.add(a_p)

    answer = 0

    # ⚠ 루트 기준으로 parent 집합, not_tree(사이클이 발생한 그래프) 갱신 ⚠
    set_parent = set(find_parnets(i) for i in range(1, n + 1))
    not_tree_parent = set(find_parnets(t) for t in not_tree)

    for s in set_parent:
        if s not in not_tree_parent:
            answer += 1

    if answer == 0:
        print(f"Case {case}: No trees.")
    elif answer == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {answer} trees.")

    case += 1
