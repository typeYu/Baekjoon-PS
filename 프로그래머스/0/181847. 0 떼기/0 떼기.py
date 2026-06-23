def solution(n_str):
    idx = 0
    while idx < len(n_str):
        if n_str[idx] == '0':
            idx += 1
        else:
            break
    
    return n_str[idx:]