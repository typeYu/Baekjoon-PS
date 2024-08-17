def solution(s):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    S = s.split(' ')
    result = ''
    for i in S:
        for j in range(len(i)):
            if j == 0 and i[j] not in numbers:
                result += i[j].upper()
            elif i[j] not in numbers:
                result += i[j].lower()
            else:
                result += i[j]
        result += ' '
                
    return result[:-1]