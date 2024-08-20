def solution(n):
    n_1_count = str(bin(n)[2:]).count('1')
    while True:
        n += 1
        converted_num_1_count = str(bin(n)[2:]).count('1')
        if n_1_count == converted_num_1_count:
            return n