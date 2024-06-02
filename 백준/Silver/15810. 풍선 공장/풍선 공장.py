N, M = map(int, input().split())
balloons = list(map(int, input().split()))

start, end = min(balloons), max(balloons) * M
count = 0
while start <= end: #start와 end가 같아지는 경우까지 고려
    mid = (start + end) // 2
    make = 0
    for i in balloons:
        make += mid // i
    if make < M:
        start = mid + 1
    else:
        end = mid - 1
print(start)