N = int(input())
d = [float('inf')] * (N + 1)
d[1] = 0
check = [0] * (N + 1) # 직전 수를 체크 하기 위한 배열
for i in range(1, N):
    if d[i + 1] > d[i] + 1:
        d[i + 1] = d[i] + 1
        check[i + 1] = i

    if i * 2 <= N:
        if d[i * 2] > d[i] + 1:
            d[i * 2] = d[i] + 1
            check[i * 2] = i

    if i * 3 <= N:
        if d[i * 3] > d[i] + 1:
            d[i * 3] = d[i] + 1
            check[i * 3] = i

# 연산 횟수 출력
answer = d[N]
print(answer)

# 방법 출력
print(N, end=' ')
while True:
    if N == 1:
        break
    print(check[N], end=' ')
    N = check[N]
