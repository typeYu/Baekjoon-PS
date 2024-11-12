import sys
S = list(sys.stdin.readline().strip())
real_num = ''
for i in S:
    real_num += i
real_num = int(real_num)
visited = {i: False for i in range(len(S))}
all_array = []

def backtracking(string):
    global visited

    if len(string) == len(S):
        new_int = int(string)
        all_array.append(new_int)
        return

    for i in range(len(S)):
        if not visited[i]:
            visited[i] = True
            string += S[i]
            backtracking(string)
            string = string[:-1]
            visited[i] = False

backtracking('')
all_array.sort()
is_big = False
for i in all_array:
    if i == real_num:
        is_big = True
    elif is_big:
        print(i)
        exit()
print(0)