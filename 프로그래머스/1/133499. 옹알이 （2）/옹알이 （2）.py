def solution(babbling):
    answer = 0
    for word in babbling:
        idx = 0
        before = ''
        while len(word) > idx:
            if word[idx:idx + 3] == 'aya' and before != 'aya':
                before = 'aya'
                idx += 3
            elif word[idx:idx + 2] == 'ye' and before != 'ye':
                before = 'ye'
                idx += 2
            elif word[idx:idx + 3] == 'woo' and before != 'woo':
                before = 'woo'
                idx += 3
            elif word[idx:idx + 2] == 'ma' and before != 'ma':
                before = 'ma'
                idx += 2
            else:
                break
        else:
            answer += 1
    
    return answer