import sys
from bisect import bisect_left
N = int(sys.stdin.readline())
array = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    array.append((a, b))
array.sort(key= lambda x: x[0])

lis = []
dp = [0] * N

for i in range(N):
    index = bisect_left(lis, array[i][1])
    if len(lis) == 0 or lis[-1] < array[i][1]:
        lis.append(array[i][1])
    else:
        lis[index] = array[i][1]
    dp[i] = index

except_list = set()
num = len(lis) - 1
for i in range(N - 1, -1, -1):
    if dp[i] == num:
        except_list.add(array[i][0])
        num -= 1

print(N - len(lis))
for i in array:
    if i[0] not in except_list:
        print(i[0])
