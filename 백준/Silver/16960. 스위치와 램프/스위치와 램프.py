N, M = map(int, input().split())
switch = []
for i in range(N):
    inputSwitch = list(map(int, input().split()))
    switch.append(inputSwitch[1:])

def isLight(switch):
    for i in range(N): # 꺼진 스위치
        lamp = [False] * M
        for j in range(N): # 켜진 스위치
            if i == j:
                continue
            else:
                for k in switch[j]:
                    lamp[k - 1] = True
        if all(lamp):
            return 1
    return 0

print(isLight(switch))