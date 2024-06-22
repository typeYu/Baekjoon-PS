import sys
N, M = map(int, sys.stdin.readline().split())
cake = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0 # 결과
isTenMulti = [] # 10으로 나누어 떨어지는 롤케이크 개수
big = 0 # 10보다 크고 나누어 떨어지지 않는 수 개수
for i in cake:
    if i == 10:
        result += 1
    elif i > 10 and i % 10 == 0:
        isTenMulti.append(i)
    elif i > 10:
        big += i // 10
isTenMulti.sort(reverse=True)

while M > 0:
    if isTenMulti:
        q = isTenMulti.pop()
        divide = q - 10
        if divide == 10:
            result += 2
        else:
            isTenMulti.append(divide)
            result += 1
    else:
        if big == 0:
            break
        result += 1
        big -= 1
    M -= 1

print(result)

