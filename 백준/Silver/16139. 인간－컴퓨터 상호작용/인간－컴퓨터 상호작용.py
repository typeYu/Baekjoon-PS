import sys
S = sys.stdin.readline().strip()
q = int(sys.stdin.readline())
count = [[0] * 26]
for i in range(len(S)):
    count.append(count[-1][:])
    count[-1][ord(S[i]) - 97] += 1

for _ in range(q):
    a, l, r = sys.stdin.readline().strip().split()
    result = count[int(r) + 1][ord(a) - 97] - count[int(l)][ord(a) - 97]
    print(result)