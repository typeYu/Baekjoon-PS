from itertools import combinations
L = int(input())
array = list(map(int, input().split()))
array.sort()
n = int(input())
numArray = []
for i in range(len(array) - 1):
    a, b = array[i], array[i + 1]
    if a == n:
        print(0)
        exit()
    if a > n:
        for j in range(1, a):
            numArray.append(j)
        break
    if a < n < b:
        for j in range(a+1, b):
            numArray.append(j)
        break
comb = combinations(numArray, 2)
count = 0
for num1, num2 in comb:
    if num1 <= n <= num2:
        count += 1
print(count)