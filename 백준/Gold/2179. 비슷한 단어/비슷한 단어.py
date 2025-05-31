import sys
N = int(sys.stdin.readline())
word = []
for i in range(N):
    word.append([sys.stdin.readline().strip(), i])

answer_cnt = 0
answer = [(word[0][1], word[0][0]), (word[1][1], word[1][0])]

word.sort()
for i in range(0, N - 1):
    S1, S2 = word[i][0], word[i + 1][0]
    S1_idx, S2_idx = word[i][1], word[i + 1][1]
    cnt = 0
    if S1 == S2:
        continue
    for j in range(min(len(S1), len(S2))):
        if S1[j] == S2[j]:
            cnt += 1
        else:
            break

    if cnt == 0:
        continue

    if answer_cnt < cnt:
        answer = [(S1_idx, S1), (S2_idx, S2)]
        answer_cnt = cnt
    elif answer_cnt == cnt:
        answer.append((S1_idx, S1))
        answer.append((S2_idx, S2))

answer.sort()
first_answer = answer[0][1]
print(first_answer)
for i in range(1, len(answer)):
    if answer[i][1] != first_answer and first_answer[:answer_cnt] == answer[i][1][:answer_cnt]:
        print(answer[i][1])
        exit()