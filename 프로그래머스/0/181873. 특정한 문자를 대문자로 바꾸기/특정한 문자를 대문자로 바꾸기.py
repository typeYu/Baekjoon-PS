def solution(my_string, alp):
    answer = ''
    for s in list(my_string):
        if s in list(alp):
            answer += s.upper()
        else:
            answer += s
    return answer