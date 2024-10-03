N = int(input())
dic = {}
for _ in range(N):
    S = input()
    for s in range(len(S)):
        if S[s] in dic:
            dic[S[s]] += 10 ** (len(S) - s - 1)
        else:
            dic[S[s]] = 10 ** (len(S) - s - 1)

descending = sorted(dic.values(), reverse=True)
multi, result = 9, 0
for d in descending:
    result += d * multi
    multi -= 1

print(result)