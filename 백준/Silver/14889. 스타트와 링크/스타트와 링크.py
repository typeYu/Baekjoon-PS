# 조합 만들 때 last_index 변수를 사용해서 팀원 조합을 중복해서 계산하는 것을 방지하는 것 주의
import sys
N = int(sys.stdin.readline())
half = N // 2
stat = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
all_stat = {}
visited = [False] * N
answer = float('inf')

# 점수 조합 미리 계산
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        all_stat[i, j] = stat[i][j]

def choice(depth, last_index): # 팀 별 사람 수, 조합을 위한 마지막 고른 사람 인덱스
    global answer

    if depth == half:
        score1, score2 = 0, 0

        # 팀별로 점수 추가
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                elif visited[i] and visited[j]:
                    score1 += all_stat[i, j]
                elif not visited[i] and not visited[j]:
                    score2 += all_stat[i, j]

        gap = abs(score1 - score2)
        if answer > gap:
            answer = gap
        return

    for i in range(last_index, N): # 재귀로 다시 for문을 돌릴 때 마지막 변수의 인덱스 + 1부터 계산
        if not visited[i]:
            visited[i] = True
            choice(depth + 1, i + 1)
            visited[i] = False

choice(0, 0)
print(answer)