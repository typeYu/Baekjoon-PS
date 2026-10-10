def solution(babbling):
    words = {"aya", "ye", "woo", "ma"}
    answer = 0
    for b in babbling:
        word = ''
        for bb in b:
            word += bb
            if word in words:
                word = ''
        
        if word == '':
            answer += 1
    
    return answer