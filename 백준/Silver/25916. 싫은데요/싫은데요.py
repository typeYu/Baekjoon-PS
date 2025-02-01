import sys
N, M = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))

start, end = 0, 0
hamster = array[start]
answer = 0
while start <= end < N:
    if hamster == M:
        answer = M
        break
    elif hamster < M or start == end:
        end += 1
        if end == N:
            break
        hamster += array[end]
    else:
        hamster -= array[start]
        start += 1

    if hamster < M:
        answer = max(hamster, answer)

print(answer)