import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    
    def find_parents(a):
        if a not in parents:
            return a
        
        parents[a] = find_parents(parents[a])
        return parents[a]
        
    parents = dict()
    answer = []
    
    for r in room_number:
        p_r = find_parents(r)
        parents[p_r] = find_parents(p_r + 1)
        answer.append(p_r)
        
    return answer