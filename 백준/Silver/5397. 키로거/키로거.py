from collections import deque

# 테스트 케이스 수 입력
t = int(input())

for _ in range(t):
    # 각 테스트 케이스에 대해 입력 받기
    s = input()

    # 비밀번호를 만들기 위한 리스트
    left_stack = []
    right_stack = deque()

    for char in s:
        if char == '<':
            # 왼쪽 화살표: 왼쪽 스택에서 하나를 오른쪽 스택으로 이동
            if left_stack:
                right_stack.appendleft(left_stack.pop())
        elif char == '>':
            # 오른쪽 화살표: 오른쪽 스택에서 하나를 왼쪽 스택으로 이동
            if right_stack:
                left_stack.append(right_stack.popleft())
        elif char == '-':
            # 백스페이스: 왼쪽 스택에서 하나를 삭제
            if left_stack:
                left_stack.pop()
        else:
            # 그 외의 문자: 왼쪽 스택에 추가
            left_stack.append(char)

    # 결과 출력: 왼쪽 스택 + 오른쪽 스택을 그대로 사용
    print(''.join(left_stack) + ''.join(right_stack))
