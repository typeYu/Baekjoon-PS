# 배낭문제인 것을 생각하지 못한 문제.
import sys


def find_parents(idx):
    if parents[idx] != idx:
        parents[idx] = find_parents(parents[idx])

    return parents[idx]


def union(one, two):
    one_parent = find_parents(one)
    two_parent = find_parents(two)

    if one_parent != two_parent:
        if one_parent < two_parent:
            parents[two_parent] = one_parent
        else:
            parents[one_parent] = two_parent


N, M, K = map(int, sys.stdin.readline().strip().split())
candy = list(map(int, sys.stdin.readline().strip().split()))
candy.insert(0, 0)
parents = [i for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())

    a_p = find_parents(a)
    b_p = find_parents(b)
    if a_p != b_p:
        union(a, b)

dic = dict()
for child in range(1, N + 1):
    c_p = find_parents(child)
    if child == c_p:
        dic[child] = [candy[child], 1]
    else:
        dic[c_p][0] += candy[child]
        dic[c_p][1] += 1

candies_and_people = list(dic.values())
L = len(candies_and_people)
candies_and_people.insert(0, [0, 0])
dp = [[0] * K for _ in range(L + 1)]

for i in range(1, L + 1):
    candies, total = candies_and_people[i]
    for j in range(1, K):
        if j < total:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - total] + candies)

print(dp[-1][-1])