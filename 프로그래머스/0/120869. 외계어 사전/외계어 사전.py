def solution(spell, dic):
    spell = set(spell)
    for d in dic:
        s = set()
        for dd in d:
            if dd in s:
                break
            s.add(dd)
        
        if spell == s:
            return 1
    
    return 2