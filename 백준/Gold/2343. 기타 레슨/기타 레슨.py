import sys
N, M = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))

start, end = max(array), sum(array) # start가 max보다 작은 값은 나올 수 없다

while start <= end:
    mid = (start + end) // 2

    total, count = 0, 1 # count를 1로 해야 하는 이유: 블루레이를 partition으로 나눌 때 마지막 건 세지 않으므로 1로 시작
    for a in array:
        if total + a > mid:
            total = 0
            count += 1
        total += a

    if count <= M:
        end = mid - 1
    else:
        start = mid + 1

print(start)
