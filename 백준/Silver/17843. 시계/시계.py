import sys

input = sys.stdin.readline

def solve():
    h, m, s = map(int, input().split())
    arr = [0] * 3
    arr[0] = 3600 * h + 60 * m + s
    arr[1] = 720 * m + 12 * s
    arr[2] = 720 * s
    arr.sort()
    mx = min(arr[1] - arr[0], arr[2] - arr[1], 43200 + arr[0] - arr[2])
    print(f"{mx / 120:.10f}")

T = int(input())
for _ in range(T):
    solve()