import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
array.sort()

answer = 0
for i in range(N):
    start, end = 0, N - 1
    while start < end:
        if array[start] + array[end] == array[i]:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                answer += 1
                break
        elif array[start] + array[end] > array[i]:
            end -= 1
        else:
            start += 1

print(answer)