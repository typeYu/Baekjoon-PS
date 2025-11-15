# 문제 설명 거지같다..
import sys
N, M = map(int, sys.stdin.readline().strip().split())
money = []
for _ in range(N):
    money.append(int(sys.stdin.readline()))

start, end = max(money), sum(money)
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    prefix_sum = 0
    for m in money:
        prefix_sum += m
        if prefix_sum > mid:
            cnt += 1
            prefix_sum = m
            if cnt > M:
                break

    if cnt > M: # cnt가 너무 많으면 범위를 늘려야 하니까 end = mid + 1
        start = mid + 1
    else: # cnt가 M이랑 같거나 적으면 범위를 좁혀야 하니까 start = mid - 1
        end = mid - 1

print(start)