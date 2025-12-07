import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))

answer, speed = 1, 1 # 제일 마지막 스피드는 1이어야
for i in range(N - 2, -1, -1):
    if speed < array[i]:
        speed += 1
    else:
        speed = min(speed, array[i])
    answer += speed

print(answer)
