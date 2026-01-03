T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    M = int(input())
    B = list(map(int, input().split()))

    K = int(input())
    C = list(map(int, input().split()))

    lucky = []

    for a in A:
        for b in B:
            for c in C:
                total = a + b + c
                sum_ = total
                good = True

                while sum_ > 0:
                    if sum_ % 10 not in [5, 8]:
                        good = False
                        break
                    sum_ //= 10

                if good:
                    lucky.append(total)

    lucky = list(set(lucky))
    print(len(lucky))
