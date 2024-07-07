N, M = map(int, input().split())
graph = [[] for _ in range(M)]
for _ in range(N):
    S = input()
    for s in range(M):
        graph[s].append(S[s])

distance = 0
answer = []
for g in graph:
    dic = {}
    for s in g:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1

    dicSorted = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    answer.append(dicSorted[0][0])
    for i in range(1, len(dicSorted)):
        distance += dicSorted[i][1]

for i in answer:
    print(i, end="")
print()
print(distance)