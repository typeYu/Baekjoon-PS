def solution(n):
    array = []
    while n > 0:
        if n % 2 != 0:
            array.append("수")
        else:
            array.append("박")
        n -= 1
    array.reverse()
    return "".join(array)