def solution(myString, pat):
    myString = myString.replace('A', 'b').replace('B', 'a')
    return 1 if pat in myString.upper() else 0