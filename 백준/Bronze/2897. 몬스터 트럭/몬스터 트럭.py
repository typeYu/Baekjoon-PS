def space(n, m, arr):
    s = []
    for x in range(2):
        for y in range(2):
            s.append(arr[n + x][m + y])
    return s

r, c = map(int, input().split())
parking_lot = [input() for _ in range(r)]
result = [0, 0, 0, 0, 0]
for i in range(r - 1):
    for j in range(c - 1):
        parking = space(i, j, parking_lot)
        if '#' in parking:
            continue
        result[parking.count('X')] += 1
for cnt in result:
    print(cnt)