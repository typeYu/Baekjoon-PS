for i in range(1, int(input()) + 1):
    S = input().split(' ')
    print(f"Case #{i}: ", end='')
    for j in range(len(S) - 1, - 1, - 1):
        print(S[j], end=' ')
    print()
