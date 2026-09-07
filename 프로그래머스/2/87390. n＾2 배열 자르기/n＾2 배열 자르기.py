def solution(n, left, right):
    ans = []
    for index in range(left, right + 1):
        row = index // n
        column = index % n
        
        ans.append(max(row, column) + 1)
    
    return ans