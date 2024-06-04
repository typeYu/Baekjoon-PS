from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    files = list(map(int, input().split()))
    array = deque([])
    for num, rank in enumerate(files):
        array.append((num, rank))
    count = 0
    while array:
        if array[0][1] != max(files):
            num = array.popleft()
            array.append(num)
        else:
            count += 1
            files.remove(array[0][1])
            num = array.popleft()
            if num[0] == M:
                break
    print(count)