# 첫 번째와 마지막 블록을 제외한 모든 현재 위치 블록에서 양쪽의 max값에서 더 적은 값에 현재 블록 값 빼주면 됨 
H, W = map(int, input().split())
block = list(map(int, input().split()))

result = 0
for i in range(1, W):
    rightMax, leftMax = 0, 0
    for j in range(i):
        rightMax = max(rightMax, block[j])
    for k in range(i + 1, W):
        leftMax = max(leftMax, block[k])

    ans = min(rightMax, leftMax) - block[i]
    if ans >= 0:
        result += ans

print(result)