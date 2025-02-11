import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
result = 0
for i in range(1, N + 1):
    result += abs(arr[i - 1] - i)

print(result)