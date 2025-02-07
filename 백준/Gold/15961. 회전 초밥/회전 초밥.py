import sys
from collections import deque
N, d, k, c = map(int, sys.stdin.readline().strip().split())

belt = []
for _ in range(N):
    belt.append(int(sys.stdin.readline()))

# 초기 세팅
current = dict()
for i in range(k):
    if belt[i] in current:
        current[belt[i]] += 1
    else:
        current[belt[i]] = 1

result = len(current)
start, end = 0, k
while True:
    # current 딕셔너리에서 1 올라간 인덱스의 시작 값을 빼주고 끝 값을 더해줌
    current[belt[start]] -= 1
    if current[belt[start]] == 0:
        current.pop(belt[start])
    if belt[end] in current:
        current[belt[end]] += 1
    else:
        current[belt[end]] = 1

    # 만약 current에 쿠폰 번호 c가 존재한다면 딕셔너리의 길이를 결과값에 추가하고, 아니라면 1을 더해 결과값에 추가
    if c in current:
        result = max(result, len(current))
    else:
        result = max(result, len(current) + 1)

    # 양쪽 끝 인덱스 1씩 올려주기
    start += 1
    if start == N:
        break
    end += 1
    if end == N:
        end = 0

print(result)