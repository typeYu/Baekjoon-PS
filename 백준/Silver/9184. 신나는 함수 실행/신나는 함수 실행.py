import sys
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # a, b, c 값이 이미 저장 되어 있으면 출력을 해줌
    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]

while True:
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a == -1 and b == -1 and c == -1:
        break
    answer = w(a, b, c)
    print("w(%d, %d, %d) = %d" % (a, b, c, answer))