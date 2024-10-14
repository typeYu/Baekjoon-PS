import sys
N, C = map(int, sys.stdin.readline().strip().split())
house = []
for _ in range(N):
    h = int(sys.stdin.readline())
    house.append(h)

house.sort()

def find():
    start, end = 1, house[-1]
    while start <= end:
        mid = (start + end) // 2
        last, count = 0, 1 # 직전 집의 인덱스, mid 만큼의 거리로 공유기를 설치했을 때 설치되는 공유기 수
        for i in range(1, N):
            if house[i] - house[last] >= mid:
                last = i
                count += 1
        if count < C:
            end = mid - 1
        else:
            start = mid + 1

    return end

print(find())