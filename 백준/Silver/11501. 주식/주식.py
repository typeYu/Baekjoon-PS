import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    array = list(map(int, sys.stdin.readline().strip().split()))
    array.reverse()
    maxNum = array[0]
    result = 0
    for i in array:
        if i > maxNum:
            maxNum = i
        result += maxNum - i
    print(result)