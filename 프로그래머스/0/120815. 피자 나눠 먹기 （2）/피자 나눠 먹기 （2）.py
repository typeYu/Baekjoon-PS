from math import gcd

def solution(n):
    answer = n // gcd(n, 6)
    return answer