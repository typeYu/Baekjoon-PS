def solution(s, skip, index):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    
    for a in s:
        idx = alphabet.index(a) # 현재 인덱스
        limit = 0
        while limit < index:
            idx = (idx + 1) % 26
            if alphabet[idx] in skip:
                continue
            else:
                limit += 1
        
        answer += alphabet[idx]
    
    return answer