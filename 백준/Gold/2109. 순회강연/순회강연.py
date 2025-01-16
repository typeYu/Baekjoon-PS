# 처음에는 적은 날짜 순서로 정렬해서 강연료가 높으면 무조건 결과 값에 저장하는 방식으로 풀이
# 그러나 나중 날짜에 저장한 결과 값보다 더 큰 강연료 값이 올 수도 있기 때문에 결과 값을 저장할 우선순위큐 사용
import sys
import heapq
N = int(sys.stdin.readline())
lectures = []
for _ in range(N):
    p, d = map(int, sys.stdin.readline().strip().split())
    lectures.append([p, d])

lectures.sort(key=lambda x: x[1]) # 날짜가 적은 순으로 정렬 ***

hq = [] # 강연료 결과를 저장할 배열. 배열 크기가 날짜이다
for i in range(N):
    pay, d_day = lectures[i] # 날짜가 적은 순서대로 정렬 된 데이터를 순서대로 꺼냄
    heapq.heappush(hq, pay) # hq에 우선순위 큐로 비용을 넣음
    if len(hq) > d_day: # 만약 데이터의 날짜보다 우선순위 큐의 크기가 클 경우 ***
        heapq.heappop(hq) # 가장 작은 값을 빼 준다(d_day를 초과 하는 날에 강연료를 저장하면 안되므로)

print(sum(hq))