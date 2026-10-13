def solution(numbers, hand):
    number = {0: [3, 1], 1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
    hand = 'R' if hand == 'right' else 'L'
    ly, lx = 3, 0 # 왼
    ry, rx = 3, 2 # 오
    
    answer = ''
    for n in numbers:
        if n in [1, 4, 7]:
            ly, lx = number[n]
            answer += 'L'
        elif n in [3, 6, 9]:
            ry, rx = number[n]
            answer += 'R'
        else:
            ny, nx = number[n]
            lGap, rGap = abs(ly - ny) + abs(lx - nx), abs(ry - ny) + abs(rx - nx)
            if lGap == rGap:
                answer += hand
                if hand == 'R':
                    ry, rx = ny, nx
                else:
                    ly, lx = ny, nx
            elif lGap > rGap:
                answer += 'R'
                ry, rx = ny, nx
            else:
                answer += 'L'
                ly, lx = ny, nx
        
    return answer
                
    