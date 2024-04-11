def solution(s):
    dic = {}
    result = []
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = i
            result.append(-1)
        else:
            result.append(i - dic[s[i]])
            dic[s[i]] = i
    return result