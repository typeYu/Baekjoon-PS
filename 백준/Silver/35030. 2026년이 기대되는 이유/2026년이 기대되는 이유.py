import sys

def sosu(N):
    if N == 1:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

def divide(N):
    s = str(N)
    for i in range(1, len(s)):
        a = int(s[:i])
        b = int(s[i:])
        if not sosu(a * b + 1):
            return False
    return True

count = [0] * (100000 + 1) # 누적합
total = 0

for num in range(1, 100000 + 1):
    if sosu(num + 1) and divide(num):
        total += 1
    count[num] = total

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(count[N])
