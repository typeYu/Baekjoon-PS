N, M = map(int, input().split())
array = []
for _ in range(N):
    array.append(int(input()))

array.sort()

start, end = min(array), max(array) * M
def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        people = 0
        for i in array:
            people += mid // i

        if people >= M:
            end = mid - 1
        else:
            start = mid + 1

    return start

print(binary_search(start, end))
