N, C = map(int, input().split())
answer = set()
for _ in range(N):
    bang = int(input())
    new_bang = bang
    while new_bang <= C:
        answer.add(new_bang)
        new_bang += bang

print(len(answer))