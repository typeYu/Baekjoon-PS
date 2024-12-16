import sys
T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().strip().split()))

sumA, sumB = 0, 0
for i in range(n):
    sumA += A[i]
    A[i] = sumA

for i in range(m):
    sumB += B[i]
    B[i] = sumB

A.insert(0, 0)
B.insert(0, 0)

dicA = {}
for i in range(1, n + 1):
    for j in range(i):
        if A[i] - A[j] in dicA:
            dicA[A[i] - A[j]] += 1
        else:
            dicA[A[i] - A[j]] = 1

answer = 0
for i in range(1, m + 1):
    for j in range(i):
        if T - (B[i] - B[j]) in dicA:
            answer += dicA[T - (B[i] - B[j])]

print(answer)