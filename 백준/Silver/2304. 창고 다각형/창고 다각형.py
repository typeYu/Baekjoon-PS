# 자꾸 스택으로 풀게 되고, 입력 말고도 한 번 탐색 하면서 스택으로 넣고 자꾸 다시 탐색하면서 답을 구하려고 함
# 입력 개수가 최대 1000개밖에 되지 않으므로 배열을 1000(1부터니까 1001)개 선언해주고 입력받을 때 높이를 입력해 준 다음
# 제일 중요: 최대 높이를 저장해준 후 왼쪽 부분 오른쪽 부분 나눠서 풀면 좋음(오목한 부분 없으니 산 모양으로 점점 줄어드는 형태로)
# 1000개의 배열을 탐색하면서 최대 높이 왼쪽 부분 차례대로 최대 높이만큼 더하고
# 오른쪽부터도 역순으로 최대 높이만큼 더해주면서 구함
import sys
N = int(sys.stdin.readline())
array = [0] * 1001
max_height, max_h_idx = 0, 0
for _ in range(N):
    location, height = map(int, sys.stdin.readline().strip().split())
    array[location] = height
    if max_height < height:
        max_height, max_h_idx = height, location

answer, cur_max = 0, 0
for i in range(max_h_idx + 1): # 왼쪽 + max기둥
    cur_max = max(cur_max, array[i])
    answer += cur_max

cur_max = 0
for i in range(1000, max_h_idx, -1): # 오른쪽
    cur_max = max(cur_max, array[i])
    answer += cur_max

print(answer)