N = int(input())
def sosu(N):
    if N == 1:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

array = []
for i in range(1, N + 1):
    if sosu(i):
        array.append(i)

end, interval_sum = 0, 0
result = 0
for start in range(len(array)):
    while interval_sum < N and end < len(array):
        interval_sum += array[end]
        end += 1

    if interval_sum == N:
        result += 1
    interval_sum -= array[start]

print(result)