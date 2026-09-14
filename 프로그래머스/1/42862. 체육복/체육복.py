def solution(n, lost, reserve):
    lost, reserve = set(lost) - set(reserve), set(reserve) - set(lost)
    reserve = {r: 0 for r in reserve}
    
    for l in lost:
        if l - 1 in reserve and reserve[l - 1] == 0:
            reserve[l - 1] = 1
        elif l + 1 in reserve and reserve[l + 1] == 0:
            reserve[l + 1] = 1
    
    return n - len(lost) + sum(reserve.values())
    
                    
            