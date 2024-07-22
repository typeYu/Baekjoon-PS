# 설명 드럽게 헷갈리게 써놓은 문제
N = int(input())
room = [list(input()) for _ in range(N)]
row, col = 0, 0
for i in range(N): # 가로
    temp = 0
    for j in range(N):
        if room[i][j] == '.':
            temp += 1
        else:
            if temp >= 2:
                row += 1
            temp = 0
    if temp >= 2:
        row += 1


for i in range(N): # 세로
    temp = 0
    for j in range(N):
        if room[j][i] == '.':
            temp += 1
        else:
            if temp >= 2:
                col += 1
            temp = 0
    if temp >= 2:
        col += 1

print(row, col)