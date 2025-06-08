import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    arr = []
    total = 0
    for i in range(1, n + 1):
        num = int(sys.stdin.readline())
        arr.append((num, i))
        total += num

    arr.sort(key=lambda x: -x[0])
    max_num = arr[0][0]
    if arr[1][0] == max_num:
        print("no winner")
    else:
        if max_num > total / 2:
            print(f"majority winner {arr[0][1]}")
        else:
            print(f"minority winner {arr[0][1]}")