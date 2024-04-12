N, M = map(int, input().split())
six, each = [], []
for _ in range(M):
    a, b = map(int, input().split())
    six.append(a)
    each.append(b)
six.sort()
each.sort()
result = 0
minNum = min(six[0], each[0] * 6)
result += (N // 6) * minNum
result += min(six[0], each[0] * (N % 6))
print(result)