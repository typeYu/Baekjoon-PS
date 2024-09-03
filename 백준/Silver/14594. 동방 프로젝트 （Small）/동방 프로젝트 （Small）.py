N = int(input())
wall = {}
for i in range(1, N): # 숫자는 각 벽 왼쪽의 숫자가 i라는 뜻
    wall[i] = 1
M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    for i in range(x, y):
        if i in wall:
            wall[i] -= 1

result = 0
for d in range(1, N):
    if wall[d] == 1:
        result += 1

print(result + 1)