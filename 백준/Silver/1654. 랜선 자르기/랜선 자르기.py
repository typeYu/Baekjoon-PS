K, N = map(int, input().split())
array = []
for _ in range(K):
    array.append(int(input()))
start = 1
end = max(array)
while (start <= end):
    count = 0
    mid = (start + end) // 2
    for x in array:
        count += x // mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
