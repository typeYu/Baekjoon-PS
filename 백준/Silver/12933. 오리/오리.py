import sys
S = sys.stdin.readline().strip()
dic = {'u': 'q', 'a': 'u', 'c': 'a', 'k': 'c'}
visited = [False] * len(S)
counting = [0] * 5  # 'q', 'u', 'a', 'c', 'k' 각각의 개수를 추적
quack = "quack"

if len(S) % 5 != 0:  # 길이가 5의 배수가 아니면 잘못된 울음
    print(-1)
    sys.exit()

# 울음 소리 추적
for i in range(len(S)):
    c = S[i]
    if c == 'q':  # 새로운 울음 시작
        if counting[4] > 0:  # 끝나지 않은 오리 울음이 있다면
            counting[4] -= 1
        counting[0] += 1  # 'q' 카운트
    elif c == 'u':
        if counting[0] > 0:
            counting[0] -= 1
            counting[1] += 1  # 'u' 카운트
        else:
            print(-1)
            sys.exit()
    elif c == 'a':
        if counting[1] > 0:
            counting[1] -= 1
            counting[2] += 1  # 'a' 카운트
        else:
            print(-1)
            sys.exit()
    elif c == 'c':
        if counting[2] > 0:
            counting[2] -= 1
            counting[3] += 1  # 'c' 카운트
        else:
            print(-1)
            sys.exit()
    elif c == 'k':
        if counting[3] > 0:
            counting[3] -= 1
            counting[4] += 1  # 'k' 카운트
        else:
            print(-1)
            sys.exit()

# 모든 오리 울음이 끝났는지 확인
if any(counting[:4]):  # 마지막에 'k'로 끝나지 않은 경우가 있다면
    print(-1)
else:
    print(counting[4])  # 완성된 'quack'의 수
