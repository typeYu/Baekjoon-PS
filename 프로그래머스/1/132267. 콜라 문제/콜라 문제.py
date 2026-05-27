def solution(a, b, n):
    answer = 0
    while n >= a:
        moc = n // a
        n = n - (moc * a) + moc * b
        answer += moc * b
    
    return answer