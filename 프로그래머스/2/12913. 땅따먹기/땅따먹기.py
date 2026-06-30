def solution(land):
    for i in range(1, len(land)):
        prev = land[i - 1]
        
        land[i][0] = max(prev[1], prev[2], prev[3]) + land[i][0]
        land[i][1] = max(prev[0], prev[2], prev[3]) + land[i][1]
        land[i][2] = max(prev[0], prev[1], prev[3]) + land[i][2]
        land[i][3] = max(prev[0], prev[1], prev[2]) + land[i][3]
        
    return max(land[-1])