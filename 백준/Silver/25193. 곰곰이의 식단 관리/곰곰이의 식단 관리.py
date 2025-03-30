N = int(input())
S = input().strip()

c = S.count('C')
e = N - c

result = c // (e + 1)
if c % (e + 1) != 0:
    result += 1

print(result)