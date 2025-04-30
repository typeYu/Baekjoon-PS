n, k  = map(int, input().split())
mul = []

for i in range(1, k+1):
    mul.append(int(str(n*i)[::-1]))

print(max(mul))