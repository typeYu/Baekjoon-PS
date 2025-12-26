import sys
N = int(sys.stdin.readline())
answer = []
for _ in range(N):
    a, b = sys.stdin.readline().strip().split()
    answer.append([a, b])
answer.sort(key=lambda x: x[1], reverse= True)
answer.sort(key=lambda x: x[0])
for a in answer:
    print(*a)