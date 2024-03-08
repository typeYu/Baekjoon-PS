import sys
N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
array.sort()
result = 0
for i in array:
    result += i * N
    N -= 1
print(result)