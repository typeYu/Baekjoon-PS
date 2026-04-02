import sys
N, K = map(int, sys.stdin.readline().strip().split())
arr = [0] * 1000001

for _ in range(N):
    g, x = map(int, sys.stdin.readline().strip().split())
    arr[x] += g

window_size = 2 * K + 1

if window_size >= 1000001:
    print(sum(arr))
else:
    amount = sum(arr[:window_size])
    answer = amount

    for i in range(window_size, 1000001):
        amount -= arr[i - window_size]
        amount += arr[i]
        answer = max(answer, amount)

    print(answer)