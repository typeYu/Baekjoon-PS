import sys
N, K = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
array.sort()

result = float('inf')
for i in range(1, N):
    team1 = array[0] * i # 첫 번째 팀 작업 속도
    team2 = array[i] * (N - i) # 두 번째 팀 작업 속도
    if K % (team1 + team2) == 0:
        total = K // (team1 + team2)
    else:
        total = K // (team1 + team2) + 1
    result = min(result, total)

print(result)