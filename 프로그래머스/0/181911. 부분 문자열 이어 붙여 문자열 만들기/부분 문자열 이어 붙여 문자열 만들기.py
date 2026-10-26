def solution(my_strings, parts):
    answer = ''
    for k in range(len(my_strings)):
        answer += my_strings[k][parts[k][0]:parts[k][1] + 1]
    
    return answer