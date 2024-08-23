a, b = map(int, input().split())
def bangmu(a, b):
    if b == 0:
        calculate = a
    else:
        calculate = a - a * (b / 100)
    if calculate >= 100:
        return 0
    else:
        return 1
print(bangmu(a, b))
