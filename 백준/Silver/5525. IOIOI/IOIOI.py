import sys
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()
comparison = 'I'
for s in range(N):
    comparison += 'OI'

count = 0
for i in range(len(S)):
    if S[i] == "I":
        if S[i:i+len(comparison)] == comparison:
            count += 1
print(count)