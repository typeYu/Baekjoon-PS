import sys
from collections import deque
S = sys.stdin.readline().strip()
zero = []
one = deque()
for i in range(len(S)):
    if S[i] == '0':
        zero.append(i)
    else:
        one.append(i)

for i in range(len(zero) // 2):
    zero.pop()

for i in range(len(one) // 2):
    one.popleft()

zero = set(zero)
one = set(one)

answer = ''
for i in range(501):
    if i in zero:
        answer += '0'
    elif i in one:
        answer += '1'

print(answer)