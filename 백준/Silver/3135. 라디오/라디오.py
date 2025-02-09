import sys
A, B = map(int, sys.stdin.readline().strip().split())
absolute_value = [abs(A - B)]
N = int(sys.stdin.readline().strip())
for _ in range(N):
    button = int(sys.stdin.readline().strip())
    absolute_value.append(abs(B - button) + 1)

absolute_value.sort()
print(absolute_value[0])