from itertools import combinations_with_replacement
dic = {"I": 1, "V": 5, "X": 10, "L": 50}
N = int(input())
result = set()
comb = combinations_with_replacement(dic, N)
for i in comb:
    save = 0
    for j in i:
        save += dic[j]
    result.add(save)
print(len(result))
