def sosu(K):
    if K == 1:
        return False
    for i in range(2, int(K**0.5)+1):
        if K % i == 0:
            return False
    else:
        return True

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n + 1, (2 * n) + 1):
        if sosu(i):
            count += 1
    print(count)