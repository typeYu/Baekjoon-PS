def solution(s):
    nums = [1,2,3,4,5,6,7,8,9,0]
    nums = str(nums)
    if len(s) != 4 and len(s) != 6:
        return False
    else:
        for i in s:
            if i not in nums:
                return False
    return True