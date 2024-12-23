N = int(input())
if N == 1:
    print(1)
else:
    N -= 1
    i = 1
    while N > 0:
        N -= 6 * i
        i += 1
    print(i)