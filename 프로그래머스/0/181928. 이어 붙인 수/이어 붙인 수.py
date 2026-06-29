def solution(num_list):
    answer_odd, answer_even = '', ''
    for n in num_list:
        if n % 2 == 0:
            answer_odd += str(n)
        else:
            answer_even += str(n)
    
    return int(answer_odd) + int(answer_even)