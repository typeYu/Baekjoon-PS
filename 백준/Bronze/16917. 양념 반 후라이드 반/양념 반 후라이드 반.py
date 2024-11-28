A, B, C, X, Y = map(int, input().split())

result = 0
if (A + B) <= 2 * C:
    result = X * A + Y * B
else:
    minNum = min(Y, X)
    result += minNum * C * 2
    if X >= Y:
        result += (X - minNum) * A
    else:
        result += (Y - minNum) * B

if max(Y, X) * C * 2 < result:
    result = max(X, Y) * C * 2

print(result)