N = int(input())
array = [input() for _ in range(N)]
array.sort(key = lambda x: len(x))
result, count = 0, N
for i in range(N):
    for j in range(i + 1, N):
        if array[i] == array[j][:len(array[i])]:
            count -= 1
            break
print(count)