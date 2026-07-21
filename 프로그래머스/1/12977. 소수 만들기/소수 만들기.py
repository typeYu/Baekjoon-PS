from itertools import combinations

def sosu(s):
        for i in range(2, int(s ** 0.5) + 1):
            if s % i == 0:
                return False
        else:
            return True

def solution(nums):
    answer = 0
    for c in combinations(nums, 3):
        if sosu(sum(c)):
            answer += 1
    
    return answer
    