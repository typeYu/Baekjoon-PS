import sys

def binary_search(i, find):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2

        if mid != i and lego[mid] == find:
            return mid
        elif lego[mid] > find:
            end = mid - 1
        else:
            start = mid + 1
    return False

while True:
    try:
        x = int(sys.stdin.readline())
        x *= 10000000
        n = int(sys.stdin.readline())
        lego = [int(sys.stdin.readline()) for _ in range(n)]
        lego.sort()
        is_danger = False
        two_answer_index = [0, 0]

        for i in range(n):
            result = binary_search(i, x - lego[i])
            if result:
                is_danger = True
                two_answer_index = [lego[i], lego[result]]
                break

        if not is_danger:
            print("danger")
        else:
            print(f"yes {two_answer_index[0]} {two_answer_index[1]}")

    except:
        break