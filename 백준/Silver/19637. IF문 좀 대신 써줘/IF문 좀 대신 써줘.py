import sys
N, M = map(int, sys.stdin.readline().split())

title, amount = [], []
for _ in range(N):
    input1, input2 = sys.stdin.readline().rstrip().split()
    title.append(input1)
    amount.append(int(input2))

for _ in range(M):
    power = int(sys.stdin.readline())
    start, end = 0, N - 1

    while start <= end:
        mid = (start + end) // 2
        if power <= amount[mid]:
            end = mid - 1
        else:
            start = mid + 1

    print(title[start])