# 그래프 시간초과 가지치기 관련 어려운 문제 - 나중에 다시 풀어볼 것

from collections import deque

def solution(n, m, x, y, r, c, k):
    directions = {(1, 0): 'd', (0, -1): 'l', (0, 1): 'r', (-1, 0): 'u'}
    ans = ''
    queue = deque([(x - 1, y - 1, 0, '')])
    
    while queue:
        i, j, cnt, route = queue.popleft()
        
        if cnt == k:
            if i == r - 1 and  j == c - 1:
                if ans == '':
                    ans = route
                else:
                    ans = min(ans, route)
            continue
        
        for di, dj in directions.keys():
            ni, nj = i + di, j + dj
            remain_k = k - (cnt + 1) # 그 칸으로 한 발 움직인 뒤 남는 이동 횟수
            required = abs(ni - (r - 1)) + abs(nj - (c - 1)) # 그 칸에서 도착점까지 필요한 최소 이동 횟수
            calculate = required - remain_k # 이 계산이 홀수이면 불가한 경로이므로 큐에 넣지 않음
            
            if 0 <= ni < n and 0 <= nj < m and remain_k >= required and calculate % 2 == 0:
                new_route = route + directions[(di, dj)]
                queue.append((ni, nj, cnt + 1, new_route))
                break # 조건을 처음 통과한 방향 하나를 큐에 넣으면 그 칸의 나머지 방향은 건너뛰는 중요한 가지치기
    
    return ans if ans != '' else "impossible"