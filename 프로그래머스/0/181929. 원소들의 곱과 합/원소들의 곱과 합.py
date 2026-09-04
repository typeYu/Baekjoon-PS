def solution(num_list):
    a, b = 1, 0
    for n in num_list:
        a *= n
        b += n
    
    if b ** 2 > a:
        return 1
    else:
        return 0
    