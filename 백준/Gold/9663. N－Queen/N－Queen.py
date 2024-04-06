N = int(input())
array = [0] * N
def attack(N):
    for i in range(N):
        if array[i] == array[N] or abs(array[N] - array[i]) == abs(N - i):
            return False
    return True
count = 0
def backtracking(v):
    global count
    if v == N:
        count += 1
    else:
        for i in range(N):
            array[v] = i
            if attack(v):
                backtracking(v+1)
backtracking(0)
print(count)