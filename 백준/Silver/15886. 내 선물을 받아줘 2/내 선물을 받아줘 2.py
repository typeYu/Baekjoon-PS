N = int(input())
S = input()
cnt = 0
for i in range(N - 1):
    if S[i] == 'E' and S[i + 1] == 'W':
        cnt += 1
print(cnt)