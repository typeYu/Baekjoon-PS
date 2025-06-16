# import sys
# from itertools import combinations
# N, M, D = map(int, sys.stdin.readline().strip().split())
# graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
# enemy = []
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 1:
#             enemy.append((i, j))
#
# archer_locations = combinations([i for i in range(N)], 3)
# answer = 0
#
#
#
# for a, b, c in archer_locations:

import sys
N, K = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
total = sum(array)

while True:
    if total >= K:
        for i in range(N):
            K -= array[i]
            if K < 0: # 여기서 K가 0 이하일 때로 하면 답이 제대로 나오지 않는다..
                print(i + 1)
                exit()
    else:
        K -= total
        if total >= K:
            for i in range(N - 1, -1, -1):
                K -= array[i]
                if K < 0: # 여기서 K가 0 이하일 때로 하면 답이 제대로 나오지 않는다.. 
                    print(i + 1)
                    exit()

