def solution(my_string, is_suffix):
    while len(my_string) > 0:
        if my_string == is_suffix:
            return 1
        my_string = my_string[1:]
    
    return 0