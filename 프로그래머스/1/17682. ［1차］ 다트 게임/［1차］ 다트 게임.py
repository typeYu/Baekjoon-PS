def solution(dartResult):
    answer, save = [], ''
    for d in dartResult:
        if d.isdigit():
            save += d
        elif d == "S":
            answer.append(int(save))
            save = ''
        elif d == "D":
            answer.append(int(save) ** 2)
            save = ''
        elif d == "T":
            answer.append(int(save) ** 3)
            save = ''
        elif d == "*":
            if len(answer) > 1:
                answer[-1] *= 2
                answer[-2] *= 2
            elif len(answer) == 1:
                answer[-1] *= 2
        elif d == "#":
            if answer:
                answer[-1] *= (-1)
    
    return sum(answer)
            
                