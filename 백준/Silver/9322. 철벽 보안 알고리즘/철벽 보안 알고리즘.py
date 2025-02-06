import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    one = {i: 0 for i in sys.stdin.readline().strip().split()}
    two = list(sys.stdin.readline().strip().split())
    for t in range(len(two)):
        one[two[t]] = t
    idx = list(one.values()) # 이 리스트의 값을 차례로 인덱스로
    password = list(sys.stdin.readline().strip().split())

    result = ['' for _ in range(n)]
    for i in range(n):
        result[i] = password[idx[i]]

    for r in result:
        print(r, end=' ')