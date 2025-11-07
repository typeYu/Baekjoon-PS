import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

temp = [array[0]]
for i in range(1, n):
    temp.append(temp[i-1] + array[i])

answer = 0
for i in range(n - 1):
    answer += array[i] * (temp[n - 1] - temp[i])

print(answer)