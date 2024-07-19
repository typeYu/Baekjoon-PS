# 일단 최장 부분수열 길이를 구한 후 ^역으로^ 배열 d를 탐색해가며 maxD부터 1까지의 인덱스로
# 해당 수열 숫자를 찾아야 한다는 발상이 조금 어렵다
import sys
N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
d = [1] * N

for i in range(1, len(array)):
    for j in range(i):
        if array[i] > array[j]:
            d[i] = max(d[j] + 1, d[i])
maxD = max(d)
print(maxD)


result = []
for j in range(len(d) - 1, -1, -1):
    if maxD == d[j]:
        result.append(array[j])
        maxD -= 1

print(*result[::-1])
