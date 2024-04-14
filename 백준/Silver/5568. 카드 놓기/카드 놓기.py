from itertools import permutations
n = int(input())
k = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
S = permutations(array, k)
result = []
for i in S:
    word = ''
    for j in i:
        word += str(j)
    result.append(int(word))
print(len(set(result)))