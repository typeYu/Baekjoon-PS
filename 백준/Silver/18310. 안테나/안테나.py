N = int(input())
array = list(map(int, input().split()))
array.sort()
a = len(array) // 2
if len(array) % 2 != 0:
    print(array[a])
else:
    count1, count2 = 0, 0
    for i in array:
        count1 += abs(array[a-1] - i)
        count2 += abs(array[a] - i)
    if count1 <= count2:
        print(array[a-1])
    else:
        print(array[a])