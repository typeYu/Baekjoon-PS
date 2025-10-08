for _ in range(int(input())):
    N = int(input())
    answer = 0
    while True:
        if N == 6174:
            print(answer)
            answer = 0
            break

        str_N = [int(''.join(i)) for i in list(str(N))]
        biggest, shortest = '', ''
        str_N.sort(reverse=True)
        for i in str_N:
            biggest += str(i)
        str_N.sort()
        for i in str_N:
            shortest += str(i)

        answer += 1
        N = int(biggest) - int(shortest)
        if len(str(N)) != 4:
            new_N = str(N)
            for i in range(4 - len(str(N))):
                new_N += '0'
            N = int(new_N)