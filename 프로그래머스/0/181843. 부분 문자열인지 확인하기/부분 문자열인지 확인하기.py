def solution(my_string, target):
    l = len(target)
    part = my_string[:l]
    
    for i in range(len(my_string) - l + 1):
        if part == target:
            return 1
        
        if i + l < len(my_string):
            part = part[1:] + my_string[i + l]
    else:
        return 0