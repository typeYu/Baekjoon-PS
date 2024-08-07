N = int(input())
array = []
for _ in range(N):
    a, b = map(int, input().split())
    array.append((a, b))

array.sort(key=lambda x: (x[0], x[1]))

result = [0, 0]
for i in range(N):
    all_profit = 0
    for j in range(i, N):
        profit = array[i][0] - array[j][1]
        if profit <= 0:
            continue
        all_profit += profit
    if result[1] >= all_profit:
        continue
    result = [array[i][0], all_profit]

print(result[0])
