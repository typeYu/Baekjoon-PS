X = int(input())

for year in range(X + 1, 10000):
    front = year // 100
    back = year % 100
    if (front + back) ** 2 == year:
        print(year)
        break
else:
    print(-1)
