from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
width, count = 0, 0 # 넓이, 개수

def bfs(y, x):
	global count
	count += 1
	queue = deque([(y, x)])
	visited[y][x] = True
	current_width = 1

	while queue:
		y, x = queue.popleft()
		for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			ny, nx = y + dy, x + dx
			if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and graph[ny][nx] == 1:
				queue.append((ny, nx))
				visited[ny][nx] = True
				current_width += 1

	return current_width

for i in range(N):
	for j in range(M):
		if graph[i][j] == 1 and not visited[i][j]:
			current_width = bfs(i, j)
			width = max(width, current_width)

print(count, width, sep='\n')