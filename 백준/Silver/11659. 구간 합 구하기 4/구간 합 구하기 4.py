import sys
N, M = map(int, input().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(1, N): #입력 값이 크면 시간초과 나므로 누적합을 통해 구해준다.
    array[i] = array[i-1] + array[i] # 입력 받은 숫자들을 누적합 배열로 재구성
array = [0] + array #인덱스를 위해 0을 추가한다.
for _ in range(M):
    i, j = map(int, input().split())
    print(array[j] - array[i - 1])