N = input()
result = 0
for i in range(1, len(N)):
    result += int('9' + (i - 1) * '0') * i
result += (int(N) - 10 ** (len(N) - 1) + 1) * len(N)
print(result)