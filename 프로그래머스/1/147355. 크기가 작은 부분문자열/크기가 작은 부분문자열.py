def solution(t, p):
    array = []
    for i in range(len(t) - len(p) + 1):
        array.append(t[i:i+len(p)])
    count = 0
    for i in array:
        if int(i) <= int(p):
            count += 1
    return count