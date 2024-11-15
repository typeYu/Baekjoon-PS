# T = int(input())
import heapq
for test_case in range(1, 11):
    cnt = int(input())
    array = list(map(int, input().split()))
    sorted_array = sorted(array)
    cut = len(sorted_array) // 2
    min_array, max_array = sorted_array[:cut], []
    for m in sorted_array[cut:]: # max_array에는 -로 넣어줬음
        max_array.append(-m)
    heapq.heapify(min_array)
    heapq.heapify(max_array)

    answer = float('inf')
    for _ in range(cnt):
        min_num = heapq.heappop(min_array)
        max_num = -(heapq.heappop(max_array))

        minus = max_num - min_num
        answer = min(answer, minus)

        if minus <= 1:
            break
        else:
            heapq.heappush(min_array, min_num + 1)
            heapq.heappush(max_array, -(max_num - 1))

    min_num = heapq.heappop(min_array)
    max_num = -(heapq.heappop(max_array))
    minus = max_num - min_num
    answer = min(answer, minus)

    print(f"#{test_case} {answer}")