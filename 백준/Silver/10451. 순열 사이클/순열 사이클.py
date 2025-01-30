import sys
sys.setrecursionlimit(2000) # 런타임 에러 방지

def dfs(x): # DFS 함수 정의
    visited[x] = True # 방문 체크
    number = numbers[x] # 다음 방문 장소
    if not visited[number]: # 방문하지 않았다면
        dfs(number) # 재귀

for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N #방문 여부 확인
    result = 0
    
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            result += 1
    print(result)