N = int(input())
array = list(map(int, input().split()))
array.insert(0, '*')
student = int(input())
for _ in range(student):
    onetwo, num = map(int, input().split())
    if onetwo == 1:
        for i in range(num, N + 1, num):
            if array[i] == 1:
                array[i] = 0
            else:
                array[i] = 1
    elif onetwo == 2:
        if array[num] == 1:
            array[num] = 0
        else:
            array[num] = 1
        left, right = num - 1, num + 1
        while left >= 1 and right <= N and array[left] == array[right]:
            if array[left] == 1:
                array[left] = 0
                array[right] = 0
            else:
                array[left] = 1
                array[right] = 1
            left -= 1
            right += 1
for i in range(1, N+1):
    print(array[i], end=" ")
    if i % 20 == 0:
        print()