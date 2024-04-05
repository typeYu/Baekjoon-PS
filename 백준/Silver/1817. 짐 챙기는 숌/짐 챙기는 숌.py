N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    array = list(map(int, input().split()))
    weight, result = 0, 1
    array.reverse()
    for i in array:
        weight += i
        if weight > M:
            result += 1
            weight = i
    print(result)