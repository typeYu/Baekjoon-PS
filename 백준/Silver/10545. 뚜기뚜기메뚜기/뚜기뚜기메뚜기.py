import sys

data = sys.stdin.read().split()

alphabet = [
    2, 22, 222,
    3, 33, 333,
    4, 44, 444,
    5, 55, 555,
    6, 66, 666,
    7, 77, 777, 7777,
    8, 88, 888,
    9, 99, 999, 9999
]

number = [0] * 10

idx = 0
for i in range(1, 10):
    temp = int(data[idx])
    idx += 1
    number[temp] = i

s = data[idx]

out = []
prev = -1

for ch in s:
    temp = alphabet[ord(ch) - 97]

    if prev == (temp % 10):
        out.append('#')

    while temp:
        digit = temp % 10
        out.append(str(number[digit]))
        prev = digit
        temp //= 10

sys.stdout.write(''.join(out) + "\n")
