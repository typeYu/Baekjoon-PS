# "간 레벨의 최솟값을 출력합니다" : 도수 레벨을 기준으로 오름차순 정렬
# " 선호도의 합 M을 채우면서" : 정렬된 배열을 for문 탐색 하며 길이 N, 선호도 합이 M 이상이면 바로
# 출력해주고(도수 레벨은 정렬 되어 있어 지금이 제일 최소이기 떄문에)
# 아니면 heap을 이용해 선호도가 제일 낮은 것을 pop() 해주는 발상이 어려웠음

import sys
import heapq
N, M, K = map(int, sys.stdin.readline().strip().split()) # N개를 골랐을 떄 v 합은 M 이상, c 합은 K를 뺐을 때 최소로
array = []
for _ in range(K):
    v, c = map(int, sys.stdin.readline().strip().split())
    array.append([v, c]) # 선호도, 도수 레벨

array.sort(key=lambda x: x[1]) # 구해야 하는 도수 최솟값을 위해 오름차 순으로 정렬
result = [] # 길이 N만큼 저장할 배열
answer = 0 # 배열을 sum하면 시간 초과, 누적합으로
for v, c in array: # c는 지금 오름차순으로 정렬되어 있음
    heapq.heappush(result, v)
    answer += v
    if len(result) == N:
        if answer >= M: # 여기서 sum쓰면 시간 초과
            print(c) # c가 오름차순으로 정렬되어 있으므로 지금의 c가 제일 큰 값임
            exit()
        else: # 만약 선호도가 M 미만이면 선호도가 작은 것을 pop해줌
            p = heapq.heappop(result)
            answer -= p

print(-1)