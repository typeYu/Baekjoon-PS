from itertools import permutations
def solution(numbers):
    
    def sosu(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    nums, result, perm = [], [], []
    for i in numbers:
        nums.append(int(i))
    for i in range(1, len(nums)+1):
        perm += permutations(nums, i)
    new_nums = [int(("").join(map(str, k))) for k in perm]
    new_nums = set(new_nums)
    for i in new_nums:
        if sosu(i) == True:
            result.append(i)
    result.sort()
    return len(result)