T = int(input())
for _ in range(T):
    S = input().split(' ')
    for i in S:
        print(i[::-1], end=" ")