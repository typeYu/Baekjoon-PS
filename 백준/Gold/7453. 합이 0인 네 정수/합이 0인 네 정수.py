import sys
n = int(sys.stdin.readline())
arrayA, arrayB, arrayC, arrayD = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().strip().split())
    arrayA.append(a)
    arrayB.append(b)
    arrayC.append(c)
    arrayD.append(d)

array1, array2 = dict(), []
for i in range(n):
    for j in range(n):
        if arrayA[i] + arrayB[j] in array1:
            array1[arrayA[i] + arrayB[j]] += 1
        else:
            array1[arrayA[i] + arrayB[j]] = 1
        array2.append(arrayC[i] + arrayD[j])

answer = 0
for cd in array2:
    if -cd in array1:
        answer += array1[-cd]
print(answer)