def solution(players, callings):
    key_is_s, key_is_idx = {}, {}
    for i in range(len(players)):
        key_is_s[players[i]] = i
        key_is_idx[i] = players[i]
    
    
    for c in callings:
        idx = key_is_s[c]
        defeat = key_is_idx[idx - 1]
        
        key_is_s[c] -= 1
        key_is_s[defeat] += 1

        key_is_idx[key_is_s[c]] = c
        key_is_idx[key_is_s[defeat]] = defeat
    
    return list(key_is_idx.values())