N, M = map(int, input().split())
maxNum = max(N, M)
minNum = min(N, M)
print((minNum - 1) + ((maxNum - 1) * minNum))