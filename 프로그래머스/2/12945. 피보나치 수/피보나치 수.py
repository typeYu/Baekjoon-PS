def solution(n):
    fibo = [0] * 100002
    fibo[1] = 1
    fibo[2] = 1
    for i in range(3, 100001):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    
    return fibo[n] % 1234567