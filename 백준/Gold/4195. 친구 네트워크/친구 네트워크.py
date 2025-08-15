import sys
sys.setrecursionlimit(100000)


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
            count[a_p] += count[b_p] # union 할 때 count 수 루트 노드에 기록하기만 해도 시간 단축 가능 ****
        else:
            parents[a_p] = b_p
            count[b_p] += count[a_p]


for _ in range(int(sys.stdin.readline())):
    parents = dict()
    count = dict()  # 시간 초과 방지
    for _ in range(int(sys.stdin.readline())):
        T1, T2 = sys.stdin.readline().strip().split()

        for T in (T1, T2):
            if T not in parents:
                parents[T] = T
                count[T] = 1

        union_parents(T1, T2)

        print(count[find_parents(T1)])