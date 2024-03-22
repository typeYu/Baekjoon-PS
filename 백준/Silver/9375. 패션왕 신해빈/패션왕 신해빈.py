T = int(input())
while T > 0:
    n = int(input())
    dic = {}
    for _ in range(n):
        value, key = input().split()
        if key in dic:
            dic[key] += [value]
        else:
            dic[key] = [value]
    result = []
    for i in dic.values():
        result.append(len(i))
    answer = 1
    for i in result:
        answer *= (i + 1)
    print(answer - 1)
    T -= 1