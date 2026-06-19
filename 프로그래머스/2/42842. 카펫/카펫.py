def solution(brown, yellow):
    for height in range(1, max(2, yellow // 2 + 1)):
        if yellow % height != 0:
            continue
        width = yellow // height
        
        if height * 2 + (width + 2) * 2 == brown:
            return [width + 2, height + 2]