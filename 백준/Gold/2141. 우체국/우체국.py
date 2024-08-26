# 총 인구 수의 절반을 넘어 가는 순간 위치를 구하면 됨
import sys
N = int(input())
total_people = 0
array = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    total_people += b
    array.append([a, b])

array.sort(key= lambda x: x[0]) # 아놔 정렬 해줘야

cur = 0
for a, b in array:
    cur += b
    if cur >= total_people / 2:
        print(a)
        exit()