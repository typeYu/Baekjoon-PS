import sys
sys.setrecursionlimit(1000000) # 런타임 에러 방지

n, m = map(int, sys.stdin.readline().strip().split())
sets = [i for i in range(n + 1)]


def find_parents(a):
    # if a == sets[a]:
    #     return a
    # else:
    #     answer = find_parents(sets[a])
    #
    # return answer
    # 시간복잡도를 위해 경로 압축 해줘야 함
    if a != sets[a]: # 루트 노드가 아니라면
        sets[a] = find_parents(sets[a]) # 현재 숫자에 루트 노드를 "기록" 하면서 재귀 호출

    return sets[a] # 반환할 때도 a가 아닌 sets[a]로 반환


def union_parents(a, b):
    a_p = find_parents(a)
    b_p = find_parents(b)

    if a_p != b_p:
        if a_p < b_p:
            # sets[b] = a_p # a, b에 대해 union이 일어날 때는, 각 집합의 '대표 노드' 수준에서 union이 일어나야 합니다.
            sets[b_p] = a_p
        else:
            sets[a_p] = b_p


for _ in range(m):
    num, a, b = map(int, sys.stdin.readline().strip().split())
    if num == 0:
        union_parents(a, b)
    else:
        a_p = find_parents(a)
        b_p = find_parents(b)
        if a_p == b_p:
            print("YES")
        else:
            print("NO")