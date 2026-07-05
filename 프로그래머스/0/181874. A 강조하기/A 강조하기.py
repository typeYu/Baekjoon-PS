def solution(myString):
    answer = ''
    for a in myString:
        if a == 'a' or a == 'A':
            answer += 'A'
        elif a.isupper():
            answer += a.lower()
        else:
            answer += a
            
    return answer