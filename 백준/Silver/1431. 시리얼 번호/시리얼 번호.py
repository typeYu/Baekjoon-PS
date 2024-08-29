N = int(input())
nums = ['1','2','3','4','5','6','7','8','9']
dic = {}
for _ in range(N):
    s = input()
    val = 0
    for i in s:
        if i in nums:
            val += int(i)
    dic[s] = val

result = sorted(dic.items(), key=lambda x: (len(x[0]), x[1], x[0]))
for r in result:
    print(r[0])
