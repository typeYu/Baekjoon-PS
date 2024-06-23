import sys
N = int(sys.stdin.readline())
result = []
for _ in range(N):
    result.append(int(sys.stdin.readline()))
result.sort(reverse=True)

for i in result:
    print(i)