N, M = map(int, input().split())
dic = {}
for _ in range(N):
    Team = input()
    dic[Team] = []
    for _ in range(int(input())):
        dic[Team].append(input())
for i in dic.values():
    i.sort()
for i in range(M):
    member = input()
    question = int(input())
    if question == 1:
        for j in dic.keys():
            if member in dic[j]:
                print(j)
    elif question == 0:
        for j in dic[member]:
            print(j)