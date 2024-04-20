N = int(input())
interval_sum, end = 0, 1
count = 0
for i in range(1, N+1):
    while interval_sum < N and end < N+1:
        interval_sum += end
        end += 1
    if interval_sum == N:
        count += 1
    interval_sum -= i
print(count)