from itertools import combinations
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

chicken_distance = float('inf')

house_location, chicken_store_location = [], []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house_location.append((i, j))
        elif graph[i][j] == 2:
            chicken_store_location.append((i, j))


def chicken_distance_check(c):
    sum_chicken_distance = 0

    for y, x in house_location:
        this_house_distance = 99
        for dy, dx in c:
            this_house_distance = min(this_house_distance, abs(y - dy) + abs(x - dx))
        sum_chicken_distance += this_house_distance
    return sum_chicken_distance

comb = combinations(chicken_store_location, M)
for c in comb:
    sum_c = chicken_distance_check(c)
    chicken_distance = min(chicken_distance, sum_c)

print(chicken_distance)