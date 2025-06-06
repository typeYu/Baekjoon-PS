e, f, c = map(int, input().split())
answer = 0
while e + f >= c:
    e = e + f
    answer += e // c
    e, f = e // c, e % c
print(answer)
