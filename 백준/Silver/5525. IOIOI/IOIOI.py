# 슬라이싱 쓰면 문자열 길이 * 슬라이싱 인덱스 만큼의 시간복잡도가 걸리므로
# for 문을 돌리기 보다 while문을 사용하고 인덱스를 조건에 따라 1, 때로는 2씩 늘린다.
import sys
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

count, i, comparison = 0, 0, 0 # 최종 값, 인덱스, OI가 몇번 반복되는지 N이랑 비교할 변수
while i <= M - 2:
    if S[i:i+3] == "IOI":
        i += 2
        comparison += 1
        if comparison == N:
            count += 1
            # 이 코드가 중요, IOI면 i를 2개씩 늘리면서 왔으므로 중복되는 IOIOI..를 세주기 위해 1만 빼줌
            comparison -= 1
    else:
        i += 1
        comparison = 0

print(count)