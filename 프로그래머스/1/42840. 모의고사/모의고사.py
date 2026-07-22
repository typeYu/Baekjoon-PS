def solution(answers):
    one, two, three = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans_1, ans_2, ans_3 = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            ans_1 += 1
        
        if answers[i] == two[i % 8]:
            ans_2 += 1
            
        if answers[i] == three[i % 10]:
            ans_3 += 1
    
    max_score = max(ans_1, ans_2, ans_3)
    
    answer = []
    if ans_1 == max_score:
        answer.append(1)
    if ans_2 == max_score:
        answer.append(2)
    if ans_3 == max_score:
        answer.append(3)
    
    return answer