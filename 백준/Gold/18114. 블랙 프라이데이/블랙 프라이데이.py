# 3개까지 선택할 수 있는데, 3개까지 조합을 돌리면 시간초과가 나기 때문에 1개 조합 2개 조합 구한 후
# 합쳐서 C가 되는 수가 있는지 dict로 찾는 아이디어
import sys
from itertools import combinations

N, C = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
dic = {} # 한 개 조합

for i in array:
    if i == C:
        print(1)
        exit()
    dic[i] = 1

for a, b in combinations(array, 2): # 두 개 조합
    if a + b == C:
        print(1)
        exit()
    elif C - (a + b) != a and C - (a + b) != b and C - (a + b) in dic:
        print(1)
        exit()

print(0)