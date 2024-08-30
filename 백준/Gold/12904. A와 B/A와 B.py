S = list(input())
T = list(input())

while T:
    if S == T:
        print(1)
        exit()
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()

print(0)
