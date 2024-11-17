N, K = map(int, input().split())
array = list(map(int, input().split()))
prefix_sum = sum(array[:K])
answer = sum(array[:K])
for i in range(N - K):
    temp = prefix_sum - array[i] + array[i + K]
    answer = max(answer, temp)
    prefix_sum = temp

print(answer)