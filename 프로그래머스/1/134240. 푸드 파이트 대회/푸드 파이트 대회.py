def solution(food):
    answer = ''
    ans_mid = ''
    
    for i in range(1, len(food)):
        for _ in range(int(food[i]) // 2):
            ans_mid += str(i)
    
    answer += ans_mid
    answer += '0'
    answer += ans_mid[::-1]
    
    return answer