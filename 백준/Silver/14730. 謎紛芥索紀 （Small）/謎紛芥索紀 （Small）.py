n = int(input())
total = 0
for i in range(n):
    c, k = map(int, input().split())
    total += c * k
print(total)