N = int(input())
array = list(map(int, input().split()))
array.sort()
result = 0
if len(array) % 2 == 0:
    for i in range(len(array) // 2):
        result = max(result, array[i] + array[-1])
        array.pop()

else:
    result = array.pop()
    for i in range(len(array) // 2):
        result = max(result, array[i] + array[-1])
        array.pop()

print(result)