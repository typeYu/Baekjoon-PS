N = int(input())
S = input()
answer = "NO"

for i in range(1, N):
    front = S[:i]
    back = S[N-i:]
    cnt = 0
    for j in range(len(front)):
        if front[j] != back[j]:
            cnt += 1

    if cnt == 1:
        answer = "YES"
        break

print(answer)