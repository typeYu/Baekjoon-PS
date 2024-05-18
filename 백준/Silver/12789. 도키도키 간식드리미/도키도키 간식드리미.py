from collections import deque
N = int(input())
array1 = deque(list(map(int, input().split())))
array2 = []
for i in range(1, N+1):
    if not array1 and array2[-1] != i:
        break
    while True:
        if not array1 and array2[-1] != i:
            break
        if array1 and array1[0] == i:
            array1.popleft()
            break
        elif array2 and array2[-1] == i:
            array2.pop()
            break
        else:
            if array1:
                array2.append(array1.popleft())
if array1 or array2:
    print("Sad")
else:
    print("Nice")
