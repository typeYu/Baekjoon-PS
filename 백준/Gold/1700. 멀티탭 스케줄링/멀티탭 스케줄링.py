import sys
N, K = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))

plugs = []
result = 0
for i in range(len(array)):
    if len(plugs) < N and array[i] not in plugs:
        plugs.append(array[i])
    elif array[i] in plugs:
        continue
    elif len(plugs) == N:
        eliminate = None # 제거해야 할 실제 기기
        eliminate_index = -1 # 제거해야 할 기기의 인덱스
        for p in plugs: # 1. 이제 안나오는 것 제거 2. 더 뒤에 나오는 것 제거
            if p not in array[i + 1:]:
                eliminate = p
                break
            else: # 남은 리스트 중 처음 등장 인덱스가 가장 마지막인 것을 빼야 함
                p_appear_index = array[i + 1:].index(p) + i + 1 # 남은 리스트에서 기기 p가 처음으로 등장하는 인덱스 (이게 제일 큰 것을 제거해야, i + 1 빼먹는거 조심)
                if p_appear_index > eliminate_index: # 만약 기존에 계산했던 제거해야 할 "인덱스"보다 현재 p의 인덱스가 더 크다면
                    eliminate_index = p_appear_index # 제거해야 할 인덱스를 현재 p의 인덱스로 바꿔주고
                    eliminate = p # 제거해야 할 변수에는 실제 p를 넣어줌
        plugs.remove(eliminate)
        plugs.append(array[i])
        result += 1

print(result)