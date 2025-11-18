import sys
N, X = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))

prefix_sum = sum(array[:X])
answer = prefix_sum
cnt = 1
start = 0
for end in range(X, N):
    prefix_sum -= array[start]
    prefix_sum += array[end]

    if answer < prefix_sum:
        answer = prefix_sum
        cnt = 1
    elif answer == prefix_sum:
        cnt += 1
        
    start += 1

print(answer, cnt, sep='\n') if answer != 0 else print("SAD")