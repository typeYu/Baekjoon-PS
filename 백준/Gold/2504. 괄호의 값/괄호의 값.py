S = list(input())
stack = []
answer = 0
temp = 1

for i in range(len(S)):
    s = S[i]

    # 여는 괄호일 때: 곱하기를 temp에 저장
    if s == '(' or s == '[':
        stack.append(s)
        if s == '(':
            temp *= 2
        elif s == '[':
            temp *= 3
    # 닫는 괄호일 때: temp값을 나눠준다
    elif stack and stack[-1] == '(' and s == ')':
        # 직전 괄호가 여는 괄호일 때만 값을 더해준다 ****
        if S[i - 1] == '(':
            answer += temp
        temp //= 2
        stack.pop()
    elif stack and stack[-1] == '[' and s == ']':
        if S[i - 1] == '[':
            answer += temp
        temp //= 3
        stack.pop()
    else:
        print(0)
        exit()

if len(stack) == 0:
    print(answer)
else:
    print(0)