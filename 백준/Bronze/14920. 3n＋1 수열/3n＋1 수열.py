def function(N):
    if N % 2 == 0:
        return N // 2
    else:
        return N * 3 + 1

N = int(input())
cnt = 1
while N != 1:
    result = function(N)
    cnt += 1
    N = result

print(cnt)