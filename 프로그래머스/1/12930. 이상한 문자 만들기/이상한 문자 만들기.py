def solution(s):
    array = s.split(' ')
    result = ''
    for i in array:
        for j in range(len(i)):
            if j % 2 == 0:
                result += i[j].upper()
            else:
                result += i[j].lower()
        result += ' '
    return result[0:-1]