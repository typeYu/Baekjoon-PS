N, K = map(int, input().split())
# K + (K - 1) + (K - 2) ... + 1 부터 (그 미만은 -1)
# K + (K - 1) + (K - 2) ... + 1에 K를 무한히 더한 만큼은 K - 1,
# 나머지는 K만큼 차이가 나게 된다.

sigma = 0
for i in range(1, K + 1):
    sigma += i

if N < sigma:
    print(-1)
elif (N - sigma) % K == 0:
    print(K - 1)
else:
    print(K)