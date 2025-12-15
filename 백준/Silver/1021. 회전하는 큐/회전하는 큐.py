from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
array = deque([i for i in range(1, N + 1)])
lst = list(map(int, input().split()))
answer = 0

for num in lst:
    if array[0] == num:
        array.popleft()
    else:
        copy_arr_right = deepcopy(array)
        right_cnt = 0
        while copy_arr_right[0] != num:
            copy_arr_right.rotate(1)
            right_cnt += 1

        copy_arr_left = deepcopy(array)
        left_cnt = 0
        while copy_arr_left[0] != num:
            copy_arr_left.rotate(-1)
            left_cnt += 1

        if right_cnt <= left_cnt:
            copy_arr_right.popleft()
            array = copy_arr_right
            answer += right_cnt
        else:
            copy_arr_left.popleft()
            array = copy_arr_left
            answer += left_cnt

print(answer)