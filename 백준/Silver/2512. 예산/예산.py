import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline())


def binary_search():
    start, end = 1, max(array)
    while start <= end:
        total = []
        mid = (start + end) // 2
        for i in range(N):
            if array[i] < mid:
                total.append(array[i])
            else:
                total.append(mid)

        if sum(total) == M:
            return max(total)
        elif sum(total) > M:
            end = mid - 1
        else:
            start = mid + 1

    return end


print(binary_search())
