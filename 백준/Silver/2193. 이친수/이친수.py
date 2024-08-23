N = int(input())
d = [1] * N
for i in range(2, N):
    d[i] = d[i - 1] + d[i - 2]
print(d[N - 1])