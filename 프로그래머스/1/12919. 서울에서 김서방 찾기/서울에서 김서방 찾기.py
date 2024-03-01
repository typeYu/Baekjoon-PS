def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            a = i
    return "".join(str("김서방은 ") + f"{a}에 " + str("있다"))