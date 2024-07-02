N = int(input())
d = [0] * 21
d[1] = 1
d[2] = 2
d[3] = 4
d[4] = 7

for i in range(5, 21):
    d[i] = d[i - 1] * 2
    if i % 2 == 0:
        d[i] -= (d[i - 4] + d[i - 5])

print(d[N])