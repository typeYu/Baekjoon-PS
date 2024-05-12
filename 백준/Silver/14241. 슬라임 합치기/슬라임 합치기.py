N = int(input())
array = list(map(int, input().split()))
score = 0
while N > 1:
    array.sort(reverse=True)
    a = 0
    score += array[-2] * array[-1]
    a += array.pop()
    a += array.pop()
    array.append(a)
    N -= 1
print(score)