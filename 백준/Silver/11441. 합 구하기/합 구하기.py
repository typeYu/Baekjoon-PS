import sys
N = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.insert(0, 0)
for i in range(1, len(array)):
    array[i] = array[i-1] + array[i]
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(array[b] - array[a-1])