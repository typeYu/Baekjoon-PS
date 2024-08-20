import sys
N = int(input())
locationX = []
locationY = []
for _ in range(N):
    xi, yi = map(int, sys.stdin.readline().strip().split())
    locationX.append(xi)
    locationY.append(yi)

locationX.sort()
locationY.sort()

if N % 2 == 0:
    n = N // 2 - 1
else:
    n = N // 2

x, y = locationX[n], locationY[n]

result = 0
for i in range(N):
    result += abs(locationX[i] - x) + abs(locationY[i] - y)
print(result)