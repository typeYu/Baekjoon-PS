N = int(input())
dic = {}
for _ in range(N):
    name, a, b, c = input().split()
    korean, english, math = int(a), int(b), int(c)
    dic[name] = [korean, english, math]
result = sorted(dic.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))
for i in result:
    print(i[0])