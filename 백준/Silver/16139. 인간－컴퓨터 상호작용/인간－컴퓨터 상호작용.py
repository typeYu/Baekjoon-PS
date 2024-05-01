import sys
S = input()
q = int(input())
stack = [[0] * 26 for _ in range(len(S) + 1)]

for i in range(1, len(S) + 1):
    for j in range(26):
        if ord(S[i-1]) - 97 == j:
            stack[i][j] += stack[i-1][j] + 1
        else:
            stack[i][j] += stack[i - 1][j]
for _ in range(q):
    a, b, c = input().split()
    A = ord(a) - 97
    B, C = int(b), int(c)
    print(stack[C+1][A] - stack[B][A])