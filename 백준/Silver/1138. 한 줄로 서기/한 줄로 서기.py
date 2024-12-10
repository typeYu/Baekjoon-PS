N = int(input())
array = list(map(int, input().split()))
result = [0] * N
for i in range(N):
    zero_count = 0
    for j in range(N):
        if result[j] == 0 and zero_count == array[i]:
            result[j] = i + 1
            break
        elif result[j] == 0:
            zero_count += 1

print(*result)