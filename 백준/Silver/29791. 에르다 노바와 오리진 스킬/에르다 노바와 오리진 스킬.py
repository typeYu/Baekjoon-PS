import sys
N, M = map(int, sys.stdin.readline().strip().split())
nova = list(map(int, sys.stdin.readline().strip().split())) # 100초
origin = list(map(int, sys.stdin.readline().strip().split())) # 360초

nova.sort()
origin.sort()

answer1, answer2 = 0, 0
nova_time, origin_time = 0, 0
for i in nova:
    if nova_time == 0:
        nova_time = i
        answer1 += 1
    else:
        if i >= nova_time + 100:
            nova_time = i
            answer1 += 1

for i in origin:
    if origin_time == 0:
        origin_time = i
        answer2 += 1
    else:
        if i >= origin_time + 360:
            origin_time = i
            answer2 += 1

print(answer1, answer2, end=' ')



