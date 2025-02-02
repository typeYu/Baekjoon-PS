import sys
from collections import deque
N, K = map(int, sys.stdin.readline().strip().split())
S = sys.stdin.readline().strip()
stack = deque()

for i in S:
    while stack and K > 0:
        if stack[-1] < int(i): # 그리디하게 지금 들어오는 숫자 i보다 스택에 마지막에 들어간 숫자가 작다면
            stack.pop() # 제거
            K -= 1
        else:
            break
    stack.append(int(i))

# 지워야 하는 숫자가 남을 수도 있음
if K > 0:
    for k in range(K):
        stack.pop()

print(''.join(map(str, stack)))