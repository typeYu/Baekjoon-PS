def solution(cards1, cards2, goal):
    cards1.reverse()
    cards2.reverse()
    for word in goal:
        if len(cards1) != 0 and word == cards1[-1]:
            cards1.pop()
        elif len(cards2) != 0 and word == cards2[-1]:
            cards2.pop()
        else:
            return "No"
        
    return "Yes"