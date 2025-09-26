import sys
N, H = map(int, sys.stdin.readline().strip().split())
high = [0] * H

for i in range(N):
    h = int(sys.stdin.readline())

    # 석순
    if i % 2 == 0:
        high[0] += 1
        high[h] -= 1
    # 종유석
    else:
        high[H - h] += 1

for j in range(1, H):
    high[j] += high[j - 1]

answer = min(high)
cnt = 0
for h in high:
    if h == answer:
        cnt += 1

print(answer, cnt)