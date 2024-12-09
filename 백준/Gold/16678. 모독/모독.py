import sys
N = int(sys.stdin.readline())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline()))

array.sort()
num = 1
hacker = 0
for i in range(N):
    if array[i] >= num:
        hacker += abs(array[i] - num)
        num += 1
print(hacker)