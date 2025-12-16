import sys
from bisect import bisect_right


def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union_parnet(a, b):
    a_p = find_parent(a)
    b_p = find_parent(b)
    parent[a_p] = b_p # 이 문제는 무조건 큰 수가 부모


N, M, K = map(int, sys.stdin.readline().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))
chursu = list(map(int, sys.stdin.readline().strip().split()))
parent = [i for i in range(M + 1)] # index out of range 방지를 위해 M + 1개 선언

cards.sort()

for c in chursu:
    idx = bisect_right(cards, c)
    real_idx = find_parent(idx)
    print(cards[real_idx]) # 여기서 find_parent로 인덱스의 부모 찾아줘야 함
    
    union_parnet(real_idx, real_idx + 1)

