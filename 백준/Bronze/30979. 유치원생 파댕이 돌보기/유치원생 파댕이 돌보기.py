import sys
T = int(sys.stdin.readline())
N = int(sys.stdin.readline())
F = list(map(int, sys.stdin.readline().strip().split()))
print("Padaeng_i Happy" if sum(F) >= T else "Padaeng_i Cry")