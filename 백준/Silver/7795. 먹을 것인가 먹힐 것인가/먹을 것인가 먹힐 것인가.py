T = int(input())
while T > 0:
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    result = 0
    for i in A:
        count, start = 0, 0
        while True:
            if start == M or i <= B[start]:
                count += start
                break
            else:
                start += 1
        result += count
    print(result)
    T -= 1