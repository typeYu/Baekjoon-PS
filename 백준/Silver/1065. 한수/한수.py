N = int(input())

def is_arithmetic(N):
    S = str(N)
    array = []
    for s in range(len(S)):
        array.append(int(S[s]))
    if len(array) == 1:
        return True
    diff = array[0] - array[1]
    for a in range(1, len(array) - 1):
        if array[a] - array[a + 1] != diff:
            return False
    return True

count = 0
for i in range(1, N + 1):
    if is_arithmetic(i):
        count += 1

print(count)