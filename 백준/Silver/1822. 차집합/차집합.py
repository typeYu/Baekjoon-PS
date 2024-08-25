import sys
na, nb = map(int, input().split())
A = set(map(int, sys.stdin.readline().strip().split()))
B = set(map(int, sys.stdin.readline().strip().split()))
print(len(A - B))
print(*sorted(list(A - B)))