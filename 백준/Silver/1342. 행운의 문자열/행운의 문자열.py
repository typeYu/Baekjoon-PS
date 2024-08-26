from itertools import permutations
S = input()
N = len(S)
dic = {}
for i in S:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

result = 0
if len(dic) == N:
    result = 1
    while N > 1:
        result *= N
        N -= 1
    print(result)
    exit()
else:
    dont = 0 # 한 글자가 몇 개 이상이면 안됨
    if N % 2 == 0:
        dont = N // 2 + 1
    else:
        dont = N // 2 + 2
    for i in dic.values():
        if i >= dont:
            print(0)
            exit()

per = set(permutations(S, N))
for i in per:
    is_diff = False
    for j in range(1, len(i)):
        if i[j] == i[j - 1]:
            is_diff = True
            break
    if not is_diff:
        result += 1
print(result)