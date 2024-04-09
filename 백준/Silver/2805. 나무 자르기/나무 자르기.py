import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
start, end = 1, max(array)
def binary_search(start, end):
    while end >= start:
        count = 0
        mid = (start + end) // 2
        for i in array:
            if i > mid:
                count += i - mid
        if count >= M:
            start = mid + 1
        else:
            end = mid - 1
    return end
print(binary_search(start, end))
