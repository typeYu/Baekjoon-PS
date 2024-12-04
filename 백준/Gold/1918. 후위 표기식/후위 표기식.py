# 개어렵다
S = input()
stack = []
result = ''
dic = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2} # 연산자 우선순위

for i in S:
    if i.isalpha():
        result += i
    elif i == '(':
        stack.append('(')
    elif i == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    else:
        while stack and dic[stack[-1]] >= dic[i]:
            result += stack.pop()
        stack.append(i)

while stack:
    result += stack.pop()

print(result)