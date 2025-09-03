import sys

N, K = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))

start, end = 0, 0
cnt = 1 if array[0] == 1 else 0 # 현재 라이언 인형 개수
answer = float('inf') # 정답 개수
while start <= end:
    # 현재 구간에서 라이언 인형이 K보다 적다면 end를 한 개씩 계속 늘림
    while end < N - 1 and cnt < K:
        end += 1
        if array[end] == 1:
            cnt += 1

    # 만약 현재 라이언 인형 개수가 K개라면 정답을 업데이트하고 start를 한 개 더한다
    if cnt == K:
        answer = min(answer, end - start + 1)
        start + 1
        if array[start] == 1:
            cnt -= 1

    start += 1

if answer == float('inf'):
    print(-1)
else:
    print(answer)