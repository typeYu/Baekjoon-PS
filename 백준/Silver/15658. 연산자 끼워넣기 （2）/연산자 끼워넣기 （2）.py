import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
operator = list(map(int, sys.stdin.readline().strip().split()))
min_answer = float('inf')
max_answer = -float('inf')


def dfs(current, idx, operator):
    global min_answer, max_answer

    if idx == N:
        min_answer = min(min_answer, current)
        max_answer = max(max_answer, current)
        return

    for o in range(4):
        if o == 0 and operator[0] > 0:
            operator[0] -= 1
            dfs(current + array[idx], idx + 1, operator)
            operator[0] += 1
        elif o == 1 and operator[1] > 0:
            operator[1] -= 1
            dfs(current - array[idx], idx + 1, operator)
            operator[1] += 1
        elif o == 2 and operator[2] > 0:
            operator[2] -= 1
            dfs(current * array[idx], idx + 1, operator)
            operator[2] += 1
        elif o == 3 and operator[3] > 0:
            operator[3] -= 1
            if current < 0:
                dfs(-(-current // array[idx]), idx + 1, operator)
            else:
                dfs(current // array[idx], idx + 1, operator)
            operator[3] += 1


dfs(array[0], 1, operator)
print(max_answer, min_answer, sep='\n')