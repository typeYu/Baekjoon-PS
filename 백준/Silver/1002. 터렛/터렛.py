import sys
from math import sqrt
for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip().split())
    distance = sqrt((x1 - x2)**2 + (y1 - y2)**2) # 두 점 사이의 거리

    # 두 원이 일치해서 교점이 무한개
    if distance == 0 and r1 == r2:
        print(-1)
    # 두 원의 교점이 2개. 두 원의 중심사이의 거리가 두 원의 반지름의 차보다 크고 합보다는 작아야
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    # 교점이 1개. 외접: 두 원의 중심사이의 거리가 두 원의 반지름의 합, 내접: 두 원의 중심사이의 거리가 두 원의 반지름의 차
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        print(1)
    # 만나지 않는 경우.
    else:
        print(0)