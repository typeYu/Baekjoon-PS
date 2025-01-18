import sys
N = int(sys.stdin.readline())
stack = []
result = 0
for i in range(N):
    height = int(sys.stdin.readline())
    start = i # 해당 높이가 적용될 수 있는 가장 왼쪽 인덱스
    while stack and stack[-1][1] > height: # 히스토그램의 높이가 줄어드는 순간에만 직사각형 계산이 필요하다는 점을 이용
        start, h = stack.pop()
        result = max(result, (i - start) * h)
    stack.append((start, height))

while stack:
    idx, h = stack.pop()
    result = max(result, (N - idx) * h)

print(result)