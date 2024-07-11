import sys
from collections import deque
T = int(sys.stdin.readline())
while T > 0:
    S = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    input_array = sys.stdin.readline().rstrip().replace('[', ',').replace(']', ',')
    split_array = input_array.split(',')
    array = []
    for i in range(1, len(split_array) - 1):
        if split_array[i]:
            array.append(int(split_array[i]))
    array = deque(array)

    reverse = False # False면 D일 때 popleft(), True면 D일 때 pop(), 마지막에 진짜로 reverse 해주기
    is_error = False
    for s in S:
        if s == 'R':
            if reverse:
                reverse = False
            else:
                reverse = True
        elif s == 'D':
            if not reverse:
                if array:
                    array.popleft()
                else:
                    is_error = True
                    break
            else:
                if array:
                    array.pop()
                else:
                    is_error = True
                    break
    if is_error:
        print("error")
    else:
        if reverse:
            array.reverse()
        print("[" + ",".join(map(str, array)) + "]")

    T -= 1
