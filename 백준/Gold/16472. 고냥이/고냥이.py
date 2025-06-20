import sys
N = int(sys.stdin.readline())
array = list(sys.stdin.readline().strip())

start, end = 0, 0
dic = {}
answer = 1
while end < len(array):
    if array[end] not in dic:
        dic[array[end]] = 1
    else:
        dic[array[end]] += 1

    while len(dic) > N:
        dic[array[start]] -= 1
        if dic[array[start]] == 0:
            dic.pop(array[start])
        start += 1

    answer = max(answer, end - start + 1)
    end += 1

print(answer)