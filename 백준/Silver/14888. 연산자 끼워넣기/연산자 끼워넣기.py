import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
operator = list(map(int, sys.stdin.readline().strip().split()))

# 초기 설정 주의: max를 0으로 설정하게 되면 결과 값이 모두 -일 때 에러
answer_max = -float('inf')
answer_min = float('inf')
def dfs(depth, result, plus, minus, multiply, divide):
    global answer_max, answer_min

    if depth == N:
        answer_max = max(answer_max, result)
        answer_min = min(answer_min, result)
        return

    if plus > 0:
        dfs(depth + 1, result + array[depth], plus - 1, minus, multiply, divide)

    if minus > 0:
        dfs(depth + 1, result - array[depth], plus, minus - 1, multiply, divide)

    if multiply > 0:
        dfs(depth + 1, result * array[depth], plus, minus, multiply - 1, divide)

    if divide > 0:
        dfs(depth + 1, int(result / array[depth]), plus, minus, multiply, divide - 1)


dfs(1, array[0], operator[0], operator[1], operator[2], operator[3])
print(answer_max)
print(answer_min)
