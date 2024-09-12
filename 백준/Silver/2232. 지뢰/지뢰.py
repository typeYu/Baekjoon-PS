N = int(input())
bombs = [0]
for _ in range(N):
    bombs.append(int(input()))
bombs.append(0)

for i in range(1, N + 1):
    if bombs[i] >= bombs[i - 1] and bombs[i] >= bombs[i + 1]:
        print(i)