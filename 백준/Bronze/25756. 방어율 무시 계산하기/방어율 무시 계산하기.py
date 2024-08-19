import sys
N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))
result, V = 0, 0

for i in array:
    result = (1 - (1 - (result / 100)) * (1 - (i / 100))) * 100
    print(round(result, 6))