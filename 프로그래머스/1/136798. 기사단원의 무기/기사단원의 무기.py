def cnt(number):
    answer = 0
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            if number // i == i:
                answer += 1
            else:
                answer += 2
    return answer

def solution(number, limit, power):
    answer = 0
    for n in range(number + 1):
        c = cnt(n)
        if c > limit:
            answer += power
        else:
            answer += c
    
    return answer