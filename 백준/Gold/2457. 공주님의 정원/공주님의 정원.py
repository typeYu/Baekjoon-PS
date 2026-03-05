import sys
N = int(sys.stdin.readline())
flowers = []
for _ in range(N):
    m1, d1, m2, d2 = sys.stdin.readline().strip().split()
    d1 = '0' + d1 if len(d1) == 1 else d1
    d2 = '0' + d2 if len(d2) == 1 else d2

    start, end = int(m1 + d1), int(m2 + d2)
    flowers.append([start, end])

flowers.sort(key=lambda x: ([x[0], -x[1]]))

if flowers[0][0] > 301:
    print(0)
    exit()

answer = 0
cur = 301
idx = 0

while 1201 > cur:
    # 현재 3월 1일이고 end가 최대인 flower로 골라야 함
    maxNum = 0
    while (N > idx) and cur >= flowers[idx][0]:
        maxNum = max(maxNum, flowers[idx][1])
        idx += 1

    if maxNum == 0:
        print(0)
        exit()
    else:
        cur = maxNum
        answer += 1

print(answer)