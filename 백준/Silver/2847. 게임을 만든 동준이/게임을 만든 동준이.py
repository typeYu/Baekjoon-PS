import sys
N = int(sys.stdin.readline().strip())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().strip()))
result = 0
for i in range(N-1, 0, -1):
    if array[i] <= array[i-1]:
        result += array[i-1] - (array[i] - 1)
        array[i-1] = array[i] - 1
print(result)