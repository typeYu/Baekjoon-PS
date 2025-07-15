import sys
cnt = 1

while True:
    S = sys.stdin.readline().strip()
    if '-' in S:
        break
    stack = []
    answer = 0

    for s in S:
        if s == '{':
            stack.append('{')
        elif s == '}':
            if len(stack) > 0:
                stack.pop()
            else:
                answer += 1
                stack.append('{') # 이 부분이 핵심. stack이 비고 닫는 괄호"}"가 들어온다면 어차피 열린 괄호로 바꿔줘야 하기 때문에 열린 괄호로 바꾸고 스택에 넣음

    answer += len(stack) // 2 # stack에 열린 괄호만 있을 텐데, 절반만 닫힌 괄호로 바꿔주면 됨

    print(f"{cnt}. {answer}")
    cnt += 1