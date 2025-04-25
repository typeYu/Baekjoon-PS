n = int(input())
total, prev = 0, 0
time = []
for _ in range(n):
    temp = list(map(int, input().split()))
    time.append(sum(temp[1:]))
time.sort()
for t in time:
    total += prev + t
    prev += t
print(total)