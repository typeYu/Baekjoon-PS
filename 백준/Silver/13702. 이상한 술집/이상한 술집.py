import sys
N, K = map(int, sys.stdin.readline().strip().split())
kettles = []
for _ in range(N):
    kettle = int(sys.stdin.readline())
    kettles.append(kettle)

start, end = 1, max(kettles) # 0l를 나눠주진 않을 거니까 start는 1로 설정한다... 0으로 설정하면 맥주가 하나도 없을 때 -1이라는 이상한 값이 나오게 됨
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for k in kettles:
        if k != 0:
            cnt += k // mid

    if cnt >= K:
        start = mid + 1
    else:
        end = mid - 1

print(end)