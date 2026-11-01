def solution(survey, choices):
    
    def vertification(S, c):
        if c in [1, 2, 3]:
            return [S[0], 4 - c]
        elif c in [5, 6, 7]:
            return [S[1], c % 4]
        elif c == 4:
            return [S[0], 0]
    
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i in range(len(survey)):
        S, c = vertification(survey[i], choices[i])
        dic[S] += c
    
    answer = ""
    if dic["R"] >= dic["T"]:
        answer += "R"
    else:
        answer += "T"
    
    if dic["C"] >= dic["F"]:
        answer += "C"
    else:
        answer += "F"
    
    if dic["J"] >= dic["M"]:
        answer += "J"
    else:
        answer += "M"
    
    if dic["A"] >= dic["N"]:
        answer += "A"
    else:
        answer += "N"
    
    return answer