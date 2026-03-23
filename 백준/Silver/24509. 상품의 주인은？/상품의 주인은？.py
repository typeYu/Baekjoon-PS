from sys import stdin
input = stdin.readline

n = int(input())
student_score = [
    list(map(int, input().split())) for _ in range(n)
]

award = []
result = []

for sub in range(1, 5):
    not_award = [s for s in student_score if s[0] not in award]
    not_award.sort(key=lambda x: (-x[sub], x[0]))
    win = not_award[0][0]
    result.append(win)
    award.append(win)

print(*result)