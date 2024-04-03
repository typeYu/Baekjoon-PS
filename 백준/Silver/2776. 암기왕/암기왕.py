T = int(input())
for i in range(T):
    note1 = int(input())
    array1 = map(int, input().split())
    note2 = int(input())
    array2 = list(map(int, input().split()))
    dic1 = {}
    for i in array1:
        dic1[i] = 1
    for i in array2:
        if i not in dic1:
            print(0)
        else:
            print(1)