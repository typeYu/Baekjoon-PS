import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parents = [i for i in range(N + 1)]

def find_parents(a):
    if parents[a] != a:
        parents[a] = find_parents(parents[a]) # 경로 최적화

    return parents[a]


def union_parents(a, b):
    a_p = find_parents(a)
    b_p = find_parents(b)

    if a_p != b_p:
        if a_p < b_p:
            parents[b_p] = a_p
        else:
            parents[a_p] = b_p


for i in range(1, N + 1):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    for a in range(1, N + 1):
        one_or_two = arr[a - 1]

        if one_or_two == 0:
            continue
        else:
            union_parents(i, a)


plan = list(map(int, sys.stdin.readline().strip().split()))

if len(plan) == 1:
    print("YES")
    exit()

for i in range(len(plan) - 1):
    if parents[plan[i]] != parents[plan[i + 1]]:
    # if find_parents(plan[i]) != find_parents(plan[i + 1]):
        print("NO")
        exit()

print("YES")
