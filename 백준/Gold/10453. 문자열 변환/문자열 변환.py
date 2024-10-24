import sys
for _ in range(int(sys.stdin.readline())):
    A, B = sys.stdin.readline().strip().split()
    A_index, B_index = [], []
    # A 문자열의 a 인덱스 찾기
    for a in range(len(A)):
        if A[a] == 'a':
            A_index.append(a)
    # B 문자열의 a 인덱스 찾기
    for b in range(len(B)):
        if B[b] == 'a':
            B_index.append(b)

    result = 0
    for i in range(len(A_index)):
        if A_index[i] != B_index[i]:
            result += abs(A_index[i] - B_index[i])

    print(result)