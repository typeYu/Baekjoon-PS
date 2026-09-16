def solution(S):
    answer = []
    S = [list(map(int, s.split(','))) for s in S[2:-2].split('},{')]
    S.sort(key=len)
    current = set() # 현재까지 나온 수
    
    for lst in S:
        for num in lst:
            if num not in current:
                current.add(num)
                answer.append(num)
    
    return answer