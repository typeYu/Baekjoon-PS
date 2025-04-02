import sys
S, C = map(int, sys.stdin.readline().strip().split())
onion = []
for _ in range(S):
    onion.append(int(sys.stdin.readline()))

onion.sort()
start, end = 1, max(onion)
length = 0 # 넣을 파의 길이

while start <= end:
    mid = (start + end) // 2 # 현재 파 길이
    share = 0 # 몫

    for o in onion:
        share += o // mid

    if share < C:
        end = mid - 1
    else:
        length = max(length, mid)
        start = mid + 1

print(sum(onion) - length * C)