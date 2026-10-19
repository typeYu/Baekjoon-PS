# for문으로 문자열을 훑으며 stack에 집어넣은 숫자들이 현재 n보다 작다면 k의 감소와 함께 stack[-1]을 없애준다
# 만약 k가 남아있다면, 끝의 k자리를 없애고 출력한다

def solution(number, k):
    stack = []
    for n in number:
        while stack and k > 0:
            if stack[-1] < n:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(n)
    
    return ''.join(map(str, stack[:-k if k != 0 else None]))