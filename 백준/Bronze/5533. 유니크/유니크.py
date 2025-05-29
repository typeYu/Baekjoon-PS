n = int(input())
players = [list(map(int, input().split())) for _ in range(n)]

scores = [0] * n

for round_index in range(3):
    count = {}
    for i in range(n):
        num = players[i][round_index]
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for i in range(n):
        num = players[i][round_index]
        if count[num] == 1:
            scores[i] += num

for score in scores:
    print(score)