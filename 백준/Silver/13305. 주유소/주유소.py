import sys
N = int(sys.stdin.readline().strip())
length = list(map(int, sys.stdin.readline().strip().split()))
cityOil = list(map(int, sys.stdin.readline().strip().split()))
minOil = cityOil[0]
result = 0
for i in range(len(length)):
    if minOil > cityOil[i]:
        minOil = cityOil[i]
    result += minOil * length[i]
print(result)
