def rank(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    answer = [0, 0]
    win = set(win_nums)
    
    for l in lottos:
        if l == 0:
            answer[0] += 1
        elif l in win:
            answer[0] += 1
            answer[1] += 1
    
    return [rank(answer[0]), rank(answer[1])]