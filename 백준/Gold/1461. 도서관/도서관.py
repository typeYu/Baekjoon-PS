import sys

N, M = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))

minus = []
plus = []

for b in books:
    if b < 0:
        minus.append(b)
    else:
        plus.append(b)

minus.sort()
plus.sort(reverse=True)

max_num = 0
if minus:
    max_num = max(max_num, abs(minus[0]))
if plus:
    max_num = max(max_num, plus[0])

answer = 0

# 음수 처리
for i in range(0, len(minus), M):
    answer += abs(minus[i])

# 양수 처리
for j in range(0, len(plus), M):
    answer += plus[j]

print(answer * 2 - max_num)