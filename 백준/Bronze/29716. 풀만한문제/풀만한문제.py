import sys
J, N = map(int, sys.stdin.readline().strip().split())
answers = []
for _ in range(N):
    S = list(sys.stdin.readline().strip())
    answer = 0
    for s in S:
        if s.islower():
            answer += 2
        elif s.isupper():
            answer += 4
        elif s == ' ':
            answer += 1
        else:
            answer += 2

    answers.append(answer)

result = 0
for a in answers:
    if a <= J:
        result += 1

print(result)