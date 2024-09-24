import sys
N = int(sys.stdin.readline())
array = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    array.append([a, b])
array.sort(key=lambda x: (x[0], x[1]))
last = 0 # 각 array마다 마지막 시간
for a, b in array:
    if last <= a:
        last = a + b
    else:
        last += b

print(last)