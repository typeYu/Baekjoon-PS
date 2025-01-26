import sys
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().strip().split()))
    array.sort()
    first_num = array.pop()
    A, B = first_num, first_num # 큰 쪽, 작은 쪽
    answer = 0

    for _ in range((N - 1) // 2):
        a = array.pop()
        b = array.pop()
        answer = max(answer, A - a, B - b)
        A = a
        B = b

    if len(array) != 0:
        a = array.pop()
        answer = max(answer, A - a)
        A = a

    print(max(answer, A - B))
