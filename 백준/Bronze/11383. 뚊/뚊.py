N, M = map(int, input().split())
first = [list(input()) for _ in range(N)]
second = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        for k in range(2):
            if first[i][j] != second[i][j * 2 + k]:
                print("Not Eyfa")
                exit()

print("Eyfa")