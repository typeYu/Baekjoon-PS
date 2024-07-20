# 만약 array가 10 20 30 25 20이라고 가정할 때
# 감소 수열 d를 1 1 1 2 3 이렇게 하나씩 더할게 아니라(감소 수열 길이를 계산하는게 아니니까)
# 1 1 3 2 1 이렇게 큰 숫자가 큰 인덱스를 가지게 계산해야 더한다음 -1 빼면 ^바이토닉 수열^임
import sys
N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
d_increase = [1] * N
d_decrease = [1] * N

for i in range(1, len(array)):
    for j in range(i):
        if array[i] > array[j]:
            d_increase[i] = max(d_increase[j] + 1, d_increase[i])

array.reverse()
for i in range(1, len(array)):
    for j in range(i):
        if array[i] > array[j]:
            d_decrease[i] = max(d_decrease[j] + 1, d_decrease[i])

d_decrease.reverse()
maxLength = 0
for i in range(N):
    maxLength = max(maxLength, d_increase[i] + d_decrease[i] - 1)
print(maxLength)

