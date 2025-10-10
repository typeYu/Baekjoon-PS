import sys
N = int(sys.stdin.readline())
S = list(sys.stdin.readline().strip())
idx = 1
d_cnt = 1 if S[0] == 'D' else 0
b_cnt = S.count('B') if d_cnt == 1 else S.count('B') - 1
answer = min(d_cnt + b_cnt, N - S.count('B'), N - S.count('D'))
while idx < N:
    if S[idx] == 'B':
        b_cnt -= 1
        answer = min(answer, b_cnt + d_cnt)
    elif S[idx] == 'D':
        d_cnt += 1
    idx += 1

print(answer)