N = int(input())
d = [1] * 117
d.insert(0, 0)
for i in range(4, 117):
    d[i] = d[i - 3] + d[i - 1]

print(d[N])