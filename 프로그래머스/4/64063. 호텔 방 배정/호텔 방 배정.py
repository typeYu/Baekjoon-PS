# 나중에 다시 풀어볼 것
# 처음에 이분탐색으로 잘못 풀음: 방이 배정되면 번호를 삭제하던 방식에서, 다음 사람이 배정할 번호를 기록하는 방식(유니온 파인드)으로 전환
# 그러나 두 원소를 union하는 함수는 필요 없음 (a가 속한 집합의 대표를 찾는거지 a, b 두 집합을 합치는 게 아니라서)
# parents라는 배열을 설정하고 부모를 기록하면 10**12 개의 배열을 계속 훑느라 시간초과가 나기 때문에 딕셔너리를 사용해야 함
# p_r(실제 배정된 방) 딕셔너리에 p_r + 1(다음 배정될 방)의 find_parents(부모)를 기록한다
# 재귀 깊이 설정해주기..

import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    
    def find_parents(a): # 부모(배정될 방)를 찾아주는 함수
        if a not in parents:
            return a
        
        parents[a] = find_parents(parents[a])
        return parents[a]
        
    parents = dict()
    answer = []
    
    for r in room_number:
        p_r = find_parents(r)
        parents[p_r] = find_parents(p_r + 1) # p_r번 방은 배정됐으므로, 다음 요청에서 건너뛸 수 있도록 p_r + 1번부터 찾은 빈방을 연결한다.
        answer.append(p_r)
        
    return answer