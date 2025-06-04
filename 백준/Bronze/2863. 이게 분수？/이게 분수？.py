A, B = map(int, input().split())
C, D = map(int, input().split())

rotations = [
    (A, B, C, D),
    (C, A, D, B),
    (D, C, B, A),
    (B, D, A, C)
]

values = []
for i in range(4):
    a, b, c, d = rotations[i]
    value = a / c + b / d
    values.append((value, i))

values.sort(key=lambda x: (-x[0], x[1]))
print(values[0][1])