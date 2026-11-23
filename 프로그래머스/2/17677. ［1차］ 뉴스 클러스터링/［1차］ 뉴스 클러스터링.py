from copy import deepcopy

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    str1 = str1.split(' ')
    str2 = str2.split(' ')
    this_is_set = set()
    
    dic1 = dict()
    for S in str1:
        for i in range(len(S) - 1):
            s = S[i:i + 2]
            this_is_set.add(s)
            if s.isalpha():
                dic1[s] = dic1.get(s, 0) + 1
    
    dic2 = dict()
    for S in str2:
        for i in range(len(S) - 1):
            s = S[i:i + 2]
            this_is_set.add(s)
            if s.isalpha():
                dic2[s] = dic2.get(s, 0) + 1
    
    ans1, ans2 = 0, 0
    for s in this_is_set:
        ans1 += min(dic1.get(s, 0), dic2.get(s, 0))
        ans2 += max(dic1.get(s, 0), dic2.get(s, 0))
    
    return int((ans1 / ans2) * 65536) if ans2 != 0 else 65536
    
    
            
    
    
    