import sys
A, B, V = map(int, sys.stdin.readline().strip().split())
result = (V - B) // (A - B)
if (V - B) % (A - B) != 0:
    result += 1
print(result)