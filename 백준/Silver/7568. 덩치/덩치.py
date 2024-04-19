N = int(input())
array = []

for _ in range(N):
    weight, height = map(int, input().split())
    array.append((weight, height))

for i in array:
    num = 1
    for j in array:
        if i[0] < j[0] and i[1] < j[1]:
                num += 1
    print(num, end = " ")