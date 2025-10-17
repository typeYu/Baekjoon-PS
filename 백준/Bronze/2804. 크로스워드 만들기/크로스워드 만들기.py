A, B = input().split()
A, B = list(A), list(B)
A_len, B_len = len(A), len(B)
commonness = [0, 0]
for i in range(A_len):
    if A[i] in B:
        commonness[0] = i
        commonness[1] = B.index(A[i])
        break

answer = [['.'] * A_len for _ in range(B_len)]

for i in range(A_len):
    answer[commonness[1]][i] = A[i]

for i in range(B_len):
    answer[i][commonness[0]] = B[i]

for a in answer:
    print(''.join(map(str, a)))