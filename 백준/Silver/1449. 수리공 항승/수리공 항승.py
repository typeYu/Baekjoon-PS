import sys
N, L = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
array.sort()

start = array[0]
count = 1

for loc in array[1:]:
    if loc in range(start, start + L):
        continue
    else:
        start = loc
        count += 1

print(count)