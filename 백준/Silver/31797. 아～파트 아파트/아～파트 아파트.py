import sys

n, m = map(int, sys.stdin.readline().split())
hands = []

for i in range(1, m + 1):
    h1, h2 = map(int, sys.stdin.readline().split())
    hands.append((h1, i))
    hands.append((h2, i))

hands.sort()

result_index = (n - 1) % (2 * m)
print(hands[result_index][1])
