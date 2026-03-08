import sys
n, k = map(int, sys.stdin.readline().strip().split())
lst = list(map(int, sys.stdin.readline().strip().split()))
lst.sort()

active = 0
answer = 0
for stone in lst:
    answer += active * stone
    if k > active:
        active += 1

print(answer)