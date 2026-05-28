def solution(n, arr1, arr2):
    arr = [[' '] * n for _ in range(n)]
    
    for i in range(n):
        # arr1
        b = bin(arr1[i])[2:] # 이진수
        S = '0' * (n - len(b)) + b # 이진수가 n보다 길이가 짧으면 앞에 '0' 붙여줌
        
        for j in range(n):
            if S[j] == '1':
                arr[i][j] = '#'
        
        # arr2
        b = bin(arr2[i])[2:] # 이진수
        S = '0' * (n - len(b)) + b # 이진수가 n보다 길이가 짧으면 앞에 '0' 붙여줌
        
        for j in range(n):
            if S[j] == '1':
                arr[i][j] = '#'
        
    
    answer = []
    for i in range(n):
        make = ''
        for j in range(n):
            make += arr[i][j]
        answer.append(make)
    
    return answer
        