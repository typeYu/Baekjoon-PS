import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))

record = [0] * 1000001

for h in array:
    if record[h] > 0:
        record[h] -= 1
    record[h - 1] += 1

print(sum(record))