import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
S = list(sys.stdin.readline().strip())
hamberger, people = deque(), []

for idx, s in enumerate(S):
    if s == "H":
        hamberger.append(idx)
    else:
        people.append(idx)

answer = 0
for p in people:
    while hamberger:
        if abs(hamberger[0] - p) <= K:
            answer += 1
            hamberger.popleft()
            break
        else:
            if hamberger[0] < p:
                hamberger.popleft()
            else:
                break

print(answer)