import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    alphabet = deque(list(sys.stdin.readline().strip().split()))

    answer = deque()
    answer.append(alphabet.popleft())

    while alphabet:
        p = alphabet.popleft()

        if ord(p) <= ord(answer[0]):
            answer.appendleft(p)
        else:
            answer.append(p)

    print(''.join(answer))
