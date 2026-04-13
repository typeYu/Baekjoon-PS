import sys

N, M = map(int, sys.stdin.readline().split())
cards = []

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort(reverse=True)
    cards.append(arr)

score = [0] * N

for m in range(M):
    max_card = max(cards[n][m] for n in range(N))
    for n in range(N):
        if cards[n][m] == max_card:
            score[n] += 1

max_score = max(score)

for i in range(N):
    if score[i] == max_score:
        print(i + 1, end=' ')