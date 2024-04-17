import sys
S = sys.stdin.readline().rstrip()
result = []
for i in range(len(S)):
    result.append(S[i:])
a = sorted(result)
for i in a:
    print(i)