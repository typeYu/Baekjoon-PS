import sys
N, M = map(int, input().split())
array = list(map(int, sys.stdin.readline().strip().split()))

prefix_sum = 0
for i in range(M):
    prefix_sum += array[i]
    array[i] = prefix_sum

for i in range(N):
    want = int(sys.stdin.readline())
    if prefix_sum < want:
        print("Go away!")
    else:
        start, end = 0, M - 1
        while start <= end:
            mid = (start + end) // 2

            if array[mid] < want:
                start = mid + 1
            else:
                end = mid - 1

        print(start + 1)
