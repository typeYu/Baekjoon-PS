import sys
N = int(input())
T = []
P = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    T.append(a)
    P.append(b)

d = [0] * (N + 1)
for i in range(N):
# T[i]의 숫자 만큼 더한 값을 미래의 d에 저장함, 계속 큰 값을 계산하여 저장
    if i + T[i] <= N:
        d[i + T[i]] = max(d[i + T[i]], d[i] + P[i])
### 이 코드가 핵심, >>>>현재까지의<<<< 최대 금액을 저장해서 다음 (d[i + 1])으로 넘김
### 만약 다음 인덱스에 저장되어 있는 수가 클 수도 있으므로 max사용
    d[i + 1] = max(d[i], d[i + 1])
### 이중 for문 사용 안하는 방법

# 이 코드도 맞음 원리는 동일
# maxNum = 0
# for i in range(N):
#     maxNum = max(maxNum, d[i])
#     if i + T[i] <= N:
#         d[i + T[i]] = max(d[i + T[i]], maxNum + P[i])
print(d[N])