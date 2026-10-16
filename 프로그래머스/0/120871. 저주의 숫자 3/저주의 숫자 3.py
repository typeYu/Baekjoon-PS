def solution(n):
    arr = [0]
    
    for _ in range(100):
        num = arr[-1] + 1
        while True:
            if num % 3 == 0 or '3' in str(num):
                num += 1
            else:
                break
        arr.append(num)
    
    return arr[n]
            