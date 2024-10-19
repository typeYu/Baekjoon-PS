import sys
A, B = map(int, sys.stdin.readline().split())
primeList = [True] * (int(B ** 0.5) + 1)
primeList[1] = False

for i in range(2, int(B ** 0.5) + 1):
    if primeList[i]:
        if i * i > int(B ** 0.5):
            break
        for j in range(i**2, int(B ** 0.5) + 1, i):
            primeList[j] = False

result = 0
for i in range(1, len(primeList)):
    if primeList[i]:
        j = 2
        while i ** j <= B:
            if i ** j >= A:
                result += 1
            j += 1

print(result)