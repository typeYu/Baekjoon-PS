import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
dic = {}
for i in array:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

stack = []
result = [-1] * N
for index, num in enumerate(array):
    while stack:
        if dic[stack[-1][1]] < dic[num]:
            i, n = stack.pop()
            result[i] = num
        else:
            break
    stack.append([index, num])

print(*result)