import sys

N, M = map(int, sys.stdin.readline().split())
S = list(sys.stdin.readline().strip())

for i in range(N):
    if M == 0:
        break

    cur = ord(S[i]) - ord('0')
    need = (10 - cur) % 10

    if need <= M:
        S[i] = '0'
        M -= need

# 남은 회전은 마지막 자리에서 처리
if M > 0:
    cur = ord(S[-1]) - ord('0')
    S[-1] = chr(ord('0') + (cur + M) % 10)

print(''.join(S))
