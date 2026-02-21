import sys
N, X = map(int, sys.stdin.readline().strip().split())
array = []
answer = 0

for i in range(N):
    A, B = map(int, sys.stdin.readline().strip().split())
    array.append([A - B, i]) # 차이, 인덱스
    answer += B

X -= N * 1000 # default를 B를 먹는다고 가정하고 시작

array.sort(key=lambda x: x[0], reverse=True)

# A - B가 큰 차이 순서로 A로 바꿀 수 있는 최대한 A로 바꾼다
for dif, i in array:
    if X < 4000 or dif <= 0:
        break

    answer += dif
    X -= 4000

print(answer)