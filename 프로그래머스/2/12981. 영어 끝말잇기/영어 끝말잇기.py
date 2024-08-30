def solution(n, words):
    dic = {}
    last_word = ''
    for i in range(len(words)):
        if len(dic) != 0 and (words[i] in dic or last_word != words[i][0]):      
            return [i % n + 1, i // n + 1]
        else:
            dic[words[i]] = 1
            last_word = words[i][-1]
    
    return [0, 0]