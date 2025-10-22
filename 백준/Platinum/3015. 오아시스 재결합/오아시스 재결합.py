# 외워서 푸는 느낌이 강함, 나중에 다시 풀어볼 것
# 스택에 [키, 사람 수] 순서대로 저장. 만약 마지막 스택에 담긴 키가 현재 입력받은 키보다 작다면,
# 그 키의 사람 수를 정답에 더해주고 pop시킴(반복문으로). 만약 키가 작지는 않고 같다면, 사람 수 더해줌
# 7 4 7 7 이 있을 때, 마지막 7은 4를 못 본다는 것: 세 번째 숫자 7을 입력받을 때 4를 없애줘야 함
# ** 이 발상이 생각하기 어려움: 만약 반복문이 끝난 후 stack에 같지 않은 키들이 남아있다면, 그 키들은 내림차순이다.
# 따라서 1명 이상인 stack에 몇명이 있던 간에 사람이 남아 있으면 정답에 1을 더해 준다
# ( 자기 자신보다 큰, 가장 마지막에 만날 수 밖에 없는 사람이 존재함을 의미 )
# 10 9 3 2 1 8 일 때, 마지막 8은, 자신보다 작은 3, 2, 1을 모두 pop한 후 9 하나를 추가로 마주 보게 된다
import sys
N = int(sys.stdin.readline())
stack = []
answer = 0
for _ in range(N):
    people = int(sys.stdin.readline())
    cnt = 1
    while stack and stack[-1][0] <= people:
        answer += stack[-1][1]
        if stack[-1][0] == people:
            cnt += stack[-1][1]
        stack.pop()

    if stack:
        answer += 1

    stack.append([people, cnt])

print(answer)

# 키가 큰 사람이 없으려면 1. (키 작) (키 큰) 이면 키 작은 사람은 앞으로 모든 입력되는 사람을 볼 수 없음, 스택에서 제외
# 2. (키 큰) (키 작)이면 앞으로 입력되는 사람은 키가 큰 사람을 볼 수 있음
# 3. (키 같음) (키 같음)이면 그 후에 입력되는 사람이 키가 작다면 첫 번째 사람은 영영 못보고, 키가 크거나 같다면 둘 다 볼 수 있음

# import sys
# N = int(sys.stdin.readline())
# stack = []
# answer = 0
# for _ in range(N):
#     people = int(sys.stdin.readline())
#     cnt = 1
#     while stack:
#         if stack[-1][0] <= people:
#             answer += stack[-1][1] # 입력받은 키보다 스택 마지막에 저장된 키가 작거나 같다면, 정답에 사람 수 포함
#             if stack[-1][0] == people: # 그 중에서도 입력받은 키랑 마지막에 저장 된 키가 같다면, cnt 해줌
#                 cnt += stack[-1][1]
#             stack.pop()
#         else:
#             break
# 
#     # 반복문이 끝난 뒤에도 stack에 사람이 남아 있다면, 마지막 한명을 answer에 추가해줌 ( 제일 마지막에 보게 되는 큰 사람 )
#     if stack:
#         answer += 1
# 
#     stack.append([people, cnt])
# 
# print(answer)